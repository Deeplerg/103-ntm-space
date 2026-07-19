import json
import argparse
from pathlib import Path

# Mapping of the Custom recipe file names to the generated HBM file names
FILE_MAPPING = {
    "ACIDIZER.json": "hbmCrystallizer.json",
    "ARCWELDER.json": "hbmArcWelder.json",
    "ASSEMBLER.json": "hbmAssemblyMachine.json",
    "CENTRIFUGE.json": "hbmCentrifuge.json",
    "CHEMICAL PLANT.json": "hbmChemicalPlant.json",
    "IRRADIATION.json": "hbmIrradiation.json",
    "PRESS.json": "hbmPress.json",
    "SHREDDER.json": "hbmShredder.json",
    "SOLDERER.json": "hbmSoldering.json"
}

def parse_custom_recipes(filepath: Path) -> list[dict]:
    """
    Reads the custom recipe file, cleans up trailing commas,
    and wraps them in brackets so they parse as a valid JSON array.
    """
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        if not content:
            return []

        content = content.rstrip(",")
        json_string = f"[{content}]"

        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse custom JSON in {filepath.name}: {e}")
        return []
    except Exception as e:
        print(f"[ERROR] Could not read {filepath.name}: {e}")
        return []

def _format_recipe(recipe: dict) -> str:
    """Formats a single recipe object according to HBM's specific rules."""
    lines = []
    for key, value in recipe.items():
        # If it's a list containing other lists or dicts, split it across multiple lines
        if isinstance(value, list) and any(isinstance(x, (list, dict)) for x in value):
            inner_items = [f'        {json.dumps(x, separators=(",", ":"))}' for x in value]
            inner_block = ",\n".join(inner_items)
            lines.append(f'      "{key}": [\n{inner_block}\n      ]')
        else:
            # Primitives and flat lists stay on one single line
            val_str = json.dumps(value, separators=(',', ':'))
            lines.append(f'      "{key}": {val_str}')

    # Join all keys with a comma and newline, wrapped in the recipe's braces
    recipe_body = ",\n".join(lines)
    return f'    {{\n{recipe_body}\n    }}'

def dump_hbm_format(data: dict) -> str:
    """
    Custom JSON stringifier that perfectly matches HBM's formatting style
    to prevent massive git diffs caused by standard python json.dump().
    """
    top_lines = []
    for key, value in data.items():
        if key == "recipes" and isinstance(value, list):
            # Format each recipe and join them with commas
            recipes_block = ",\n".join(_format_recipe(r) for r in value)
            top_lines.append(f'  "{key}": [\n{recipes_block}\n  ]')
        else:
            # Generic top-level keys (like "comment")
            val_str = json.dumps(value, separators=(',', ':'))
            top_lines.append(f'  "{key}": {val_str}')

    # Join the top level keys and wrap in the root braces
    body = ",\n".join(top_lines)
    return f'{{\n{body}\n}}\n'

def merge_recipes(custom_recipes: list[dict], hbm_filepath: Path, dry_run: bool) -> bool:
    """
    Loads the target HBM JSON, checks for duplicates via deep equality,
    appends new recipes, and saves the file preserving HBM formatting.
    """
    try:
        with open(hbm_filepath, "r", encoding="utf-8") as f:
            hbm_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Target HBM file {hbm_filepath.name} contains invalid JSON: {e}")
        return False

    if "recipes" not in hbm_data or not isinstance(hbm_data["recipes"], list):
        print(f"[WARNING] 'recipes' array not found in {hbm_filepath.name}. Skipping.")
        return False

    base_recipes = hbm_data["recipes"]
    added_count = 0

    for custom_recipe in custom_recipes:
        if custom_recipe not in base_recipes:
            base_recipes.append(custom_recipe)
            added_count += 1

    if added_count > 0:
        if not dry_run:
            formatted_json = dump_hbm_format(hbm_data)
            with open(hbm_filepath, "w", encoding="utf-8") as f:
                f.write(formatted_json)
                f.write('\n') # Ensure trailing newline

        action = "Would add" if dry_run else "Added"
        print(f"[+] {action} {added_count} new recipe(s) to {hbm_filepath.name}")
    else:
        print(f"[*] {hbm_filepath.name} is already up to date (no new recipes).")

    return True

def main():
    parser = argparse.ArgumentParser(description="Merge custom recipes into HBM generated recipes.")
    parser.add_argument("-c", "--custom-dir", type=Path, default=Path("CUSTOM RECIPES SPACE"),
                        help="Path to the custom recipes folder.")
    parser.add_argument("-t", "--hbm-dir", type=Path, default=Path("hbmRecipes"),
                        help="Path to the auto-generated HBM recipes folder.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be added without actually modifying the HBM files.")

    args = parser.parse_args()
    custom_dir: Path = args.custom_dir.resolve()
    hbm_dir: Path = args.hbm_dir.resolve()

    if not custom_dir.exists():
        print(f"[ERROR] Custom recipes directory not found: {custom_dir}")
        return

    if not hbm_dir.exists():
        print(f"[ERROR] HBM recipes directory not found: {hbm_dir}")
        print("Please launch the game once to generate the default HBM recipe files.")
        return

    print(f"Merging recipes from '{custom_dir.name}' into '{hbm_dir.name}'...")
    print("-" * 50)

    for custom_name, hbm_name in FILE_MAPPING.items():
        custom_filepath = custom_dir / custom_name
        hbm_filepath = hbm_dir / hbm_name

        if not custom_filepath.exists():
            print(f"[-] Skipping {custom_name} (File not found in custom folder).")
            continue

        if not hbm_filepath.exists():
            print(f"[-] Skipping {custom_name} (Target {hbm_name} not found in HBM folder).")
            continue

        custom_recipes = parse_custom_recipes(custom_filepath)
        if custom_recipes:
            merge_recipes(custom_recipes, hbm_filepath, args.dry_run)

    print("-" * 50)
    print("Finished merging recipes.")

if __name__ == "__main__":
    main()