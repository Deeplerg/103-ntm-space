import sys
import subprocess
import argparse
import urllib.parse
from pathlib import Path

# Use the built-in tomllib for Python 3.11+, fallback to tomli for older versions.
try:
    import tomllib
except ImportError:
    import tomli as tomllib


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replace CurseForge mods in a packwiz modpack with direct URL downloads."
    )
    parser.add_argument(
        "-d", "--dir",
        type=Path,
        default=Path.cwd(),
        help="Path to the packwiz modpack root (where pack.toml is). Defaults to the current directory."
    )
    parser.add_argument(
        "-p", "--packwiz",
        type=str,
        default="packwiz",
        help="Path or alias to the packwiz executable. Defaults to 'packwiz'."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without modifying files or actually running packwiz."
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress the standard output of packwiz commands."
    )
    parser.add_argument(
        "--no-force",
        action="store_true",
        help="Do not append --force to packwiz url add command."
    )
    return parser.parse_args()


def run_cmd(cmd: list[str], cwd: Path, quiet: bool, dry_run: bool) -> bool:
    """Executes a subprocess command safely."""
    if dry_run:
        print(f"    [DRY RUN] Would run: {' '.join(cmd)}")
        return True

    stdout = subprocess.DEVNULL if quiet else None
    try:
        subprocess.run(cmd, cwd=cwd, stdout=stdout, check=False)
        return True
    except FileNotFoundError:
        print(f"\n[ERROR] Packwiz executable not found: {cmd[0]}")
        print("Ensure packwiz is installed and in your PATH, or provide it via --packwiz.")
        sys.exit(1)


def generate_forgecdn_url(file_id: int | str, filename: str) -> str:
    """Calculates the direct ForgeCDN URL for a given CurseForge file ID and filename."""
    file_id_str = str(file_id)
    if len(file_id_str) > 3:
        part1 = str(int(file_id_str[:-3]))
        part2 = str(int(file_id_str[-3:]))
    else:
        part1 = "0"
        part2 = str(int(file_id_str))

    encoded_filename = urllib.parse.quote(filename)
    return f"https://mediafilez.forgecdn.net/files/{part1}/{part2}/{encoded_filename}"


def restore_side_metadata(pack_dir: Path, mod_slug: str, original_side: str, meta_folder: str) -> None:
    """Restores the original 'side' property to the newly generated packwiz TOML file."""
    target_dir = pack_dir / meta_folder

    # Restrict the search to the specific meta-folder to prevent conflicts
    new_files = list(target_dir.rglob(f"{mod_slug}.pw.toml"))
    if not new_files:
        print(f"    Warning: Could not find newly generated .pw.toml for {mod_slug} in {meta_folder} to restore side metadata.")
        return

    new_file = new_files[0]
    content = new_file.read_text(encoding="utf-8")

    if 'side = "both"' in content:
        content = content.replace('side = "both"', f'side = "{original_side}"')
        new_file.write_text(content, encoding="utf-8")
        print(f"    Restored side = '{original_side}' for {mod_slug}")


def process_mod_file(filepath: Path, pack_dir: Path, args: argparse.Namespace) -> bool:
    """
    Reads the mod metadata, checks if it's a CurseForge mod, and replaces it with a direct URL.
    Returns True if the mod was successfully replaced, False otherwise.
    """
    # Ignore main packwiz configuration files
    if filepath.name in ("pack.pw.toml", "index.pw.toml"):
        return False

    with open(filepath, "rb") as f:
        try:
            data = tomllib.load(f)
        except Exception as e:
            print(f"Skipping {filepath.relative_to(pack_dir)} (Parse error: {e})")
            return False

    # Skip if not managed by CurseForge
    if data.get("download", {}).get("mode") != "metadata:curseforge":
        return False

    cf_update = data.get("update", {}).get("curseforge", {})
    project_id = cf_update.get("project-id")
    file_id = cf_update.get("file-id")
    filename = data.get("filename")

    if not project_id or not file_id or not filename:
        print(f"Skipping {filepath.relative_to(pack_dir)} (Missing CF project-id, file-id, or filename)")
        return False

    mod_slug = filepath.name[:-8]
    original_side = data.get("side", "both")
    url = generate_forgecdn_url(file_id, filename)

    # Calculate the folder relative to the pack root (e.g. "mods" or "mods-optional")
    meta_folder = str(filepath.parent.relative_to(pack_dir))

    print(f"Processing '{mod_slug}' (CF Project: {project_id}, File: {file_id})")
    print(f"    -> Target Folder: {meta_folder}")
    print(f"    -> Target URL: {url}")

    # 1. Remove the old CurseForge mod via CLI
    rm_cmd = [args.packwiz, "remove", mod_slug]
    run_cmd(rm_cmd, cwd=pack_dir, quiet=args.quiet, dry_run=args.dry_run)

    # 2. Add the generic URL mod via CLI, respecting the original folder
    add_cmd = [args.packwiz, "url", "add", mod_slug, url, "--meta-folder", meta_folder]
    if not args.no_force:
        add_cmd.append("--force")
    run_cmd(add_cmd, cwd=pack_dir, quiet=args.quiet, dry_run=args.dry_run)

    # 3. Restore the correct side flag (client/server/both)
    if original_side != "both" and not args.dry_run:
        restore_side_metadata(pack_dir, mod_slug, original_side, meta_folder)

    print("-" * 50)
    return True


def main() -> None:
    args = parse_args()
    pack_dir = args.dir.resolve()

    if not (pack_dir / "pack.toml").exists() and not args.dry_run:
        print(f"Warning: No 'pack.toml' found in {pack_dir}.")
        print("Are you sure this is a packwiz modpack root? Proceeding anyway...\n")

    pw_files = list(pack_dir.rglob("*.pw.toml"))
    if not pw_files:
        print(f"No .pw.toml files found in {pack_dir}.")
        return

    modified_count = 0

    for filepath in pw_files:
        if process_mod_file(filepath, pack_dir, args):
            modified_count += 1

    print(f"\nFinished processing. Replaced {modified_count} CurseForge mod(s).")


if __name__ == "__main__":
    main()