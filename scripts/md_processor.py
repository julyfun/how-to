#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import subprocess
from datetime import datetime
import argparse
from pathlib import Path

def get_git_first_track_date(file_path):
    """Get the date when the file was first tracked by git"""
    try:
        # Use git log to find the first commit that added this file
        cmd = ["git", "log", "--follow", "--format=%ad", "--date=format:%Y-%m-%d %H:%M:%S", "--reverse", "--", file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        dates = result.stdout.strip().split('\n')
        if dates and dates[0]:
            return dates[0]
    except (subprocess.SubprocessError, subprocess.CalledProcessError):
        pass

    # Fallback to current datetime if git info is not available
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def extract_header(content):
    """Extract header content between first and second '---' lines

    Args:
        content: String content of a type B file

    Returns:
        Header content (without the --- delimiters)
    """
    lines = content.split('\n')
    if lines[0] != '---':
        return ""

    # Find the second ---
    second_dash_index = -1
    for i in range(1, len(lines)):
        if lines[i] == '---':
            second_dash_index = i
            break

    if second_dash_index == -1:
        return ""

    # Extract the header content (excluding the --- lines)
    header_content = lines[1:second_dash_index]
    return '\n'.join(header_content)

def get_sharp_title(content, filename):
    """Find the first line starting with '# ' and extract the title

    Args:
        content: String content of the file
        filename: Filename without extension as fallback

    Returns:
        Title extracted from the first '# ' line or filename if not found
    """
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()

    # Fallback to filename
    return filename

def recover(content, rec_title, file_path):
    """Process type B file content

    Args:
        content: String content of a type B file
        rec_title: The title to use if no title is found
        file_path: Path to the file (for git date)

    Returns:
        Processed content
    """
    lines = content.split('\n')
    if lines[0] != '---':
        raise AssertionError("File is not type B")

    # Find the second ---
    second_dash_index = -1
    for i in range(1, len(lines)):
        if lines[i] == '---':
            second_dash_index = i
            break

    if second_dash_index == -1:
        raise AssertionError("File is not type B (missing second ---)")

    # Extract the header
    header_lines = lines[1:second_dash_index]

    # Process header fields
    has_title = False
    has_tags = False

    # First pass - collect all metadata
    tags_content = []
    new_header_lines = []

    for line in header_lines:
        line = line.strip()

        # Handle title field
        if line.startswith('title:'):
            has_title = True
            new_header_lines.append(line)

        # Handle keywords field - convert to tags
        elif line.startswith('keywords:'):
            # Extract content after "keywords: "
            content = line[9:].strip()
            # remove [] 
            if content.startswith('[') and content.endswith(']'):
                content = content[1:-1].strip()
            if content:
                tags_content.append(content)
            has_tags = True  # Mark that we have tags now

        # Handle tags field
        elif line.startswith('tags:'):
            # Extract content after "tags: "
            content = line[5:].strip()
            # Strip brackets if present
            if content.startswith('[') and content.endswith(']'):
                content = content[1:-1].strip()
            if content:
                tags_content.append(content)
            has_tags = True

        # Keep other fields unchanged
        elif not line.startswith('date:'):  # We'll handle date separately
            new_header_lines.append(line)

    # Handle date field separately to avoid duplicates
    date_added = False
    for line in header_lines:
        if line.strip().startswith('date:'):
            new_header_lines.append(line.strip())
            date_added = True
            break

    # Add date if not present
    if not date_added:
        git_date = get_git_first_track_date(file_path)
        new_header_lines.append(f'date: {git_date}')

    # Add title if not present
    if not has_title:
        new_header_lines.append(f'title: {rec_title}')

    # Add tags field with all collected tags in array format
    if tags_content:
        new_header_lines.append(f'tags: [{", ".join(tags_content)}]')
    elif not has_tags:
        new_header_lines.append('tags: []')

    # Replace the original header lines with our processed ones
    header_lines = new_header_lines

    # All missing fields have been handled in the code above

    # Reconstruct the file
    new_header = '\n'.join(header_lines)
    body = '\n'.join(lines[second_dash_index + 1:])

    return f"---\n{new_header}\n---\n{body}"

def process_file(file_path):
    """Process a markdown file according to the specified rules

    Args:
        file_path: Path to the markdown file

    Returns:
        Processed content
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip empty files
    if not content.strip():
        return content

    lines = content.split('\n')
    first_line = lines[0] if lines else ""

    # Get filename without extension for fallback title
    filename = os.path.basename(file_path)
    filename_without_ext = os.path.splitext(filename)[0]

    # Extract sharp title
    rec_title = get_sharp_title(content, filename_without_ext)

    # Determine file type
    if first_line.startswith('- ') and len(first_line) >= 3 and first_line[2].islower():
        # Type A file
        dash_lines = []
        i = 0
        while i < len(lines) and lines[i].startswith('- '):
            dash_lines.append(lines[i][2:])  # Remove the "- " prefix
            i += 1

        # Create a type B header
        new_header = '\n'.join(dash_lines)
        new_content = f"---\n{new_header}\n---\n" + '\n'.join(lines[i:])

        # Process as type B
        return recover(new_content, rec_title, file_path)

    elif first_line == '---' and '---' in lines[1:]:
        # Type B file
        return recover(content, rec_title, file_path)

    else:
        # Type C file
        git_date = get_git_first_track_date(file_path)
        new_header = f"""---
title: {rec_title}
date: {git_date}
tags: []
---
"""
        return new_header + content

def process_directory(directory):
    """Process all markdown files in a directory recursively

    Args:
        directory: Directory path to process
    """
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                try:
                    processed_content = process_file(file_path)

                    # Write the processed content back to the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(processed_content)

                    count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

    print(f"Processed {count} markdown files")

def main():
    parser = argparse.ArgumentParser(description='Process markdown files in a directory')
    parser.add_argument('directory', help='Directory containing markdown files to process')
    args = parser.parse_args()

    directory = args.directory

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main()
