import os
import json
from pydantic import TypeAdapter
from models import QuestItem
import utils
import layout
import bq_generator
import config

def ensure_directories():
    """Creates necessary input and output directories."""
    dirs = [
        "data",
        f"output/betterquesting/DefaultQuests/Quests/{config.QUESTLINE_DIR_NAME}",
        f"output/betterquesting/DefaultQuests/QuestLines/{config.QUESTLINE_DIR_NAME}",
        "output/lang"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def generate_sample_data():
    """Creates sample files if the data directory is empty."""
    items_path = "data/items.json"
    if not os.path.exists(items_path):
        sample_items = [{
            "internal_name": "chlorine_pinwheel",
            "reward_id": "hbm:item.chlorine_pinwheel",
            "reward_meta": 0,
            "hours_to_acquire": 2.1
        }]
        with open(items_path, "w", encoding="utf-8") as f:
            json.dump(sample_items, f, indent=2)

    for lang in config.LANGUAGES:
        lang_path = f"data/lang_{lang}.json"
        if not os.path.exists(lang_path):
            sample_lang = {
                "chlorine_pinwheel": {
                    "name": "Chlorine Pinwheel" if lang == "en_us" else "Хлорная вертушка",
                    "desc": "Rare artifact." if lang == "en_us" else "Редкий артефакт из радиоактивных пустошей."
                }
            }
            with open(lang_path, "w", encoding="utf-8") as f:
                json.dump(sample_lang, f, indent=2, ensure_ascii=False)

def main():
    ensure_directories()
    generate_sample_data()

    # Load Items
    with open("data/items.json", "r", encoding="utf-8") as f:
        raw_items = json.load(f)

    items_adapter = TypeAdapter(list[QuestItem])
    quests = items_adapter.validate_python(raw_items)

    # Pre-load the default language dict to embed into the Quest JSONs
    default_lang_path = f"data/lang_{config.DEFAULT_LANGUAGE}.json"
    default_lang_data = {}
    if os.path.exists(default_lang_path):
        with open(default_lang_path, "r", encoding="utf-8") as f:
            default_lang_data = json.load(f)

    lang_snippets = {lang: [] for lang in config.LANGUAGES}

    for index, quest in enumerate(quests):
        q_uuid = utils.generate_deterministic_uuid(quest.internal_name)
        q_b64 = utils.uuid_to_b64(q_uuid)
        q_b64_clean = q_b64.replace("=", "")  # BQ lang files don't use padding

        camel_name = utils.snake_to_camel(quest.internal_name)
        filename = f"{camel_name}-{q_b64}.json"

        x, y = layout.get_spiral_coords(index)

        # Grab Default Language translations, fallback to internal name if missing
        lang_entry = default_lang_data.get(quest.internal_name, {})
        default_name = lang_entry.get("name", camel_name)
        default_desc = lang_entry.get("desc", quest.internal_name)

        quest_data = bq_generator.get_quest_json(q_uuid, quest, default_name, default_desc)
        line_data = bq_generator.get_questline_entry_json(q_uuid, x, y)

        q_path = f"output/betterquesting/DefaultQuests/Quests/{config.QUESTLINE_DIR_NAME}/{filename}"
        with open(q_path, "w", encoding="utf-8") as f:
            json.dump(quest_data, f, indent=2, sort_keys=True)

        l_path = f"output/betterquesting/DefaultQuests/QuestLines/{config.QUESTLINE_DIR_NAME}/{filename}"
        with open(l_path, "w", encoding="utf-8") as f:
            json.dump(line_data, f, indent=2, sort_keys=True)

        # Build localization snippets
        for lang in config.LANGUAGES:
            lang_path = f"data/lang_{lang}.json"
            if os.path.exists(lang_path):
                with open(lang_path, "r", encoding="utf-8") as f:
                    lang_data = json.load(f)

                if quest.internal_name in lang_data:
                    entry = lang_data[quest.internal_name]
                    lang_snippets[lang].append(f"\n# Quest: {camel_name}")
                    lang_snippets[lang].append(f"betterquesting.quest.{q_b64_clean}.name={entry['name']}")
                    lang_snippets[lang].append(f"betterquesting.quest.{q_b64_clean}.desc={entry['desc']}")

    # Write Lang Snippets
    for lang, lines in lang_snippets.items():
        if not lines: continue
        snippet_path = f"output/lang/admin_shop_{lang}.lang.snippet"
        with open(snippet_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    print(f"Successfully generated {len(quests)} quests into the 'output/' directory.")

if __name__ == "__main__":
    main()