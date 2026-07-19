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
    Reads the custom recipe file.
    Because the files are just raw comma-separated JSON objects and often
    have a trailing comma, we need to clean them up and wrap them in brackets
    so they parse as a valid JSON array.
    """
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        if not content:
            return []

        # Strip trailing commas that would break standard JSON parsing
        content = content.rstrip(",")

        # Wrap the raw objects in an array
        json_string = f"[{content}]"

        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse custom JSON in {filepath.name}: {e}")
        return []
    except Exception as e:
        print(f"[ERROR] Could not read {filepath.name}: {e}")
        return []

def merge_recipes(custom_recipes: list[dict], hbm_filepath: Path, dry_run: bool) -> bool:
    """
    Loads the target HBM JSON, checks for duplicates via deep equality,
    appends new recipes, and saves the file.
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
        # Python natively does deep dictionary equality checks.
        # This will perfectly match the JSON object regardless of where it is in the list!
        if custom_recipe not in base_recipes:
            base_recipes.append(custom_recipe)
            added_count += 1

    if added_count > 0:
        if not dry_run:
            with open(hbm_filepath, "w", encoding="utf-8") as f:
                # Indent of 2 closely matches the default HBM formatting
                json.dump(hbm_data, f, indent=2)

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