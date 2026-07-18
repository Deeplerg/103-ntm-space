import os
import re
from dict import *

CURRENCY="universalcoins:item.iron_coin"

QUESTS_DIR = os.path.join("config", "betterquesting", "DefaultQuests", "Quests")

def process_quests():
    if not os.path.exists(QUESTS_DIR):
        print(f"Error: Could not find directory '{QUESTS_DIR}'. Make sure you are running this from the right folder.")
        return

    count = 0
    for root, dirs, files in os.walk(QUESTS_DIR):
        for file in files:
            if file.endswith(".json") and file in REWARD_MAPPING:
                amount = REWARD_MAPPING[file]
                filepath = os.path.join(root, file)
                inject_reward(filepath, amount)
                count += 1
                
    print(f"\nSuccessfully processed {count} quest files!")

def inject_reward(filepath, amount):
    # Added newline='' to prevent automatic translation
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        lines = f.readlines()

    if not lines:
        return

    # Detect the original line separator from the first line
    nl = '\n'
    if lines[0].endswith('\r\n'):
        nl = '\r\n'
    elif lines[0].endswith('\r'):
        nl = '\r'

    # Find the starting line of the rewards block
    start_idx = -1
    for i, line in enumerate(lines):
        if '"rewards:9": {' in line or '"rewards:9": {}' in line:
            start_idx = i
            break

    if start_idx == -1:
        print(f"Warning: 'rewards:9' not found in {filepath}. Skipping.")
        return

    # Determine exact indentation to keep Git history clean
    indent_match = re.match(r'^(\s*)', lines[start_idx])
    indent = indent_match.group(1) if indent_match else ""
    inner = indent + "  "

    # Find the closing brace of the rewards block (needed for both updates and injections)
    end_idx = -1
    if "{}" not in lines[start_idx]:
        for i in range(start_idx + 1, len(lines)):
            if lines[i].startswith(indent + "}") or lines[i].startswith(indent + "},"):
                end_idx = i
                break

    # Check if currency is already in the file (Update Case)
    currency_line_idx = -1
    if end_idx != -1:
        for i in range(start_idx + 1, end_idx):
            if f'"id:8": "{CURRENCY}"' in lines[i]:
                currency_line_idx = i
                break

    # Case 0: The reward already exists, update the amount
    if currency_line_idx != -1:
        # Search nearby lines for the Count value
        for j in range(max(0, currency_line_idx - 5), min(len(lines), currency_line_idx + 5)):
            if '"Count:3":' in lines[j]:
                new_line = re.sub(r'("Count:3":\s*)\d+', r'\g<1>' + str(amount), lines[j])

                # Only write to file if the amount actually changed
                if lines[j] != new_line:
                    lines[j] = new_line
                    # Added newline='' to preserve endings on save
                    with open(filepath, 'w', encoding='utf-8', newline='') as f:
                        f.writelines(lines)
                    print(f"Updated to {amount} coins -> {os.path.basename(filepath)}")
                return
        return

    # Case 1: The rewards block is currently completely empty e.g. "rewards:9": {}
    if "{}" in lines[start_idx]:
        has_comma = "," in lines[start_idx]
        new_block = (
            f'{indent}"rewards:9": {{\n'
            f'{inner}"0:10": {{\n'
            f'{inner}  "rewardID:8": "bq_standard:item",\n'
            f'{inner}  "index:3": 0,\n'
            f'{inner}  "rewards:9": {{\n'
            f'{inner}    "0:10": {{\n'
            f'{inner}      "id:8": "{CURRENCY}",\n'
            f'{inner}      "Count:3": {amount},\n'
            f'{inner}      "Damage:2": 0,\n'
            f'{inner}      "OreDict:8": ""\n'
            f'{inner}    }}\n'
            f'{inner}  }}\n'
            f'{inner}}}\n'
            f'{indent}}}' + ("," if has_comma else "") + "\n"
        ).replace('\n', nl) # Swap hardcoded newlines for detected file endings

        lines[start_idx] = new_block

    # Case 2: The rewards block already has items (e.g. Trophies/Loot)
    else:
        if end_idx == -1:
            print(f"Warning: Could not find end of rewards block in {filepath}")
            return
        
        # Calculate the next index (e.g., if "0:10" exists, we need "1:10")
        entry_pattern = re.compile(r'^' + indent + r'  "(\d+):10": \{$')
        max_idx = -1
        for i in range(start_idx + 1, end_idx):
            m = entry_pattern.match(lines[i].rstrip('\n\r'))
            if m:
                idx = int(m.group(1))
                max_idx = max(max_idx, idx)
        
        new_idx = max_idx + 1

        # Add a comma and the detected newline to the preceding line so JSON doesn't break
        prev_line_idx = end_idx - 1
        lines[prev_line_idx] = lines[prev_line_idx].rstrip('\n\r') + "," + nl

        # Build the new reward entry
        new_entry = (
            f'{inner}"{new_idx}:10": {{\n'
            f'{inner}  "rewardID:8": "bq_standard:item",\n'
            f'{inner}  "index:3": {new_idx},\n'
            f'{inner}  "rewards:9": {{\n'
            f'{inner}    "0:10": {{\n'
            f'{inner}      "id:8": "{CURRENCY}",\n'
            f'{inner}      "Count:3": {amount},\n'
            f'{inner}      "Damage:2": 0,\n'
            f'{inner}      "OreDict:8": ""\n'
            f'{inner}    }}\n'
            f'{inner}  }}\n'
            f'{inner}}}\n'
        ).replace('\n', nl) # Swap hardcoded newlines for detected file endings

        # Inject right before the closing brace
        lines.insert(end_idx, new_entry)

    # Write changes back to the file using newline=''
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines)
    
    print(f"Added {amount} coins -> {os.path.basename(filepath)}")

if __name__ == "__main__":
    print("Starting Currency Injection...")
    process_quests()