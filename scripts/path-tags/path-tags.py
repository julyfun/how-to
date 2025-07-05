#!/usr/bin/env python3
import os
import re
import yaml
import subprocess
import sys
from typing import List, Dict, Optional, Union, Tuple
from collections import OrderedDict


# Custom YAML loader to preserve order
class OrderedLoader(yaml.SafeLoader):
    pass


# Custom YAML dumper to preserve order
class OrderedDumper(yaml.SafeDumper):
    pass


# Set up OrderedDict loader and dumper
def construct_mapping(loader, node):
    loader.flatten_mapping(node)
    return OrderedDict(loader.construct_pairs(node))


OrderedLoader.add_constructor(
    yaml.resolver.Resolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def represent_ordereddict(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.Resolver.DEFAULT_MAPPING_TAG, data.items()
    )


OrderedDumper.add_representer(OrderedDict, represent_ordereddict)


def get_all_md_files(folder_path: str) -> List[str]:
    """
    Recursively get all markdown files in the given folder.

    Args:
        folder_path: Path to the folder to search in

    Returns:
        List of absolute paths to markdown files
    """
    md_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files


def extract_front_matter(content: str) -> Optional[Dict]:
    """
    Extract front matter from markdown content, preserving the order of keys.

    Args:
        content: The markdown content as a string

    Returns:
        Dictionary of front matter or None if no front matter found
    """
    # Match content between --- or +++ delimiters at the start of the file
    pattern = r"^\s*(---|\+\+\+)\s*\n(.*?)\n\s*\1\s*\n"
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return None

    front_matter_text = match.group(2)
    try:
        # Use OrderedLoader to preserve key order
        front_matter = yaml.load(front_matter_text, Loader=OrderedLoader)
        return front_matter
    except Exception:
        # If parsing fails, return the raw text as a single string
        return OrderedDict({"raw": front_matter_text})


def get_relative_path(file_path: str) -> str:
    """
    Get the relative path of a file from the git repo root.

    Args:
        file_path: Absolute path to the file

    Returns:
        Relative path from the git repo root
    """
    try:
        # Get the git repo root directory
        git_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=os.path.dirname(file_path),
            text=True,
        ).strip()

        # Get relative path
        relative_path = os.path.relpath(file_path, git_root)
        return relative_path
    except subprocess.CalledProcessError:
        # Fallback if not in a git repo
        print(f"Warning: Could not determine git root for {file_path}")
        # Return the basename as fallback
        return os.path.basename(file_path)


def update_tags_from_path(file_path: str) -> bool:
    """
    Update tags in the front matter based on the file path, preserving key order.

    Args:
        file_path: Path to the markdown file

    Returns:
        True if the file was updated, False otherwise
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    front_matter = extract_front_matter(content)
    if front_matter is None:
        print(f"No front matter in {file_path}, skipping")
        return False

    # Get relative path from git root
    relative_path = get_relative_path(file_path)

    # Split path and get components (excluding the filename)
    path_parts = os.path.dirname(relative_path).split(os.sep)
    path_parts = [part for part in path_parts if part]  # Remove empty parts

    # Also get the filename without extension
    # filename_no_ext = os.path.splitext(os.path.basename(relative_path))[0]
    # if filename_no_ext:
    #     path_parts.append(filename_no_ext)

    # Check if tags exist in front matter
    tags = front_matter.get("tags", [])
    if isinstance(tags, str):
        # If tags is a string, convert it to a list
        tags = [tag.strip() for tag in tags.split(",")]
    elif not isinstance(tags, list):
        tags = []

    # Check if path components are in tags
    modified = False
    for part in path_parts:
        if part and part not in tags:
            tags.append(part)
            modified = True

    if not modified:
        return False

    # Update front matter with new tags
    front_matter["tags"] = tags

    # Find the front matter in the content
    pattern = r"^\s*(---|\+\+\+)\s*\n(.*?)\n\s*\1\s*\n"
    match = re.match(pattern, content, re.DOTALL)

    if match:
        delimiter = match.group(1)

        # Get the original front matter text to analyze its structure
        original_front_matter_text = match.group(2)

        # Format tags as a string with square brackets
        tags_str = ", ".join([f'"{tag}"' for tag in tags])
        tags_formatted = f"[{tags_str}]"

        # Custom YAML dump preserving order
        new_front_matter = yaml.dump(
            front_matter,
            Dumper=OrderedDumper,
            default_flow_style=False,
            allow_unicode=True,
        )

        # Replace the dash list format with square brackets format for tags
        tags_yaml_dash_format = re.compile(r"tags:(\s*\n\s*-.*)+", re.MULTILINE)
        if tags_yaml_dash_format.search(new_front_matter):
            new_front_matter = tags_yaml_dash_format.sub(
                f"tags: {tags_formatted}", new_front_matter
            )
        else:
            # If regex replacement fails, ensure tags are in the right format
            tag_line_regex = re.compile(r"tags:.*\n", re.MULTILINE)
            if tag_line_regex.search(new_front_matter):
                new_front_matter = tag_line_regex.sub(
                    f"tags: {tags_formatted}\n", new_front_matter
                )
            else:
                # If tags line doesn't exist, add it
                new_front_matter += f"tags: {tags_formatted}\n"

        # Replace old front matter with new one
        new_content = (
            f"{delimiter}\n{new_front_matter.rstrip()}\n{delimiter}\n"
            + content[match.end() :]
        )

        # Write back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Updated tags in {file_path}")
        return True

    return False


def main():
    """
    Main function to process all markdown files in the specified input path.
    """
    # Check if input path is provided
    if len(sys.argv) < 2:
        print("Usage: python3 path-tags.py <input_folder>")
        return

    # Get the input folder from command line arguments
    input_folder = sys.argv[1]

    # Resolve to absolute path
    if not os.path.isabs(input_folder):
        input_folder = os.path.abspath(input_folder)

    if not os.path.isdir(input_folder):
        print(f"Error: {input_folder} is not a directory")
        return

    # Get all markdown files in the input folder
    md_files = get_all_md_files(input_folder)
    print(f"Found {len(md_files)} markdown files in {input_folder}")

    # Process each file
    updated_count = 0
    for file_path in md_files:
        if update_tags_from_path(file_path):
            updated_count += 1

    print(f"Updated {updated_count} files")


if __name__ == "__main__":
    main()
