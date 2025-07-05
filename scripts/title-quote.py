#!/usr/bin/env python3
import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple

def get_file_type(content: str) -> str:
    """
    Determine the file type based on its content:
    - Type A: First line starts with "- " followed by a lowercase letter
    - Type B: First line is "---" and there's another "---" line later
    - Type C: Everything else
    """
    lines = content.split("\n")
    if not lines:
        return "C"
    
    first_line = lines[0].strip()
    
    # Check if it's Type A
    if first_line.startswith("- ") and len(first_line) > 2 and first_line[2].islower():
        return "A"
    
    # Check if it's Type B
    if first_line == "---" and "---" in [line.strip() for line in lines[1:]]:
        return "B"
    
    # Otherwise it's Type C
    return "C"

def extract_sharp_title(content: str, filepath: str) -> str:
    """
    Extract the first line starting with "# " as the title
    If no such line exists, use the filename without extension
    """
    for line in content.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    
    # If no "# " line is found, use the filename without extension
    return Path(filepath).stem

def header(content: str) -> str:
    """
    Extract content between the first two "---" markers
    Asserts that the file is of type B, otherwise exits with an error
    """
    file_type = get_file_type(content)
    if file_type != "B":
        print(f"Error: Expected file type B, but got {file_type}")
        sys.exit(1)
    
    try:
        # Find the positions of the first two "---" markers
        first_marker = content.find("---")
        second_marker = content.find("---", first_marker + 3)
        
        # Extract the content between the markers
        if first_marker != -1 and second_marker != -1:
            return content[first_marker + 3:second_marker].strip()
        else:
            raise ValueError("Could not find both frontmatter markers")
    except Exception as e:
        print(f"Error extracting header: {str(e)}")
        sys.exit(1)

def process_title_in_header(header_content: str) -> str:
    """
    Process the header content to ensure the title has double quotes
    """
    lines = header_content.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("title:"):
            # Extract the title part (everything after "title:")
            title_part = line.split("title:", 1)[1].strip()
            
            # Check if the title is already quoted
            if not (title_part.startswith('"') and title_part.endswith('"')):
                # Remove any existing single quotes
                if title_part.startswith("'") and title_part.endswith("'"):
                    title_part = title_part[1:-1]
                # Add double quotes
                title_part = f'"{title_part}"'
                lines[i] = f"title: {title_part}"
    
    return "\n".join(lines)

def update_file_with_quoted_title(filepath: str) -> None:
    """
    Update the file with properly quoted title in the header
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_type = get_file_type(content)
        if file_type == "B":
            # Extract the header content
            header_content = header(content)
            
            # Process the title in the header
            new_header_content = process_title_in_header(header_content)
            
            # Replace the old header with the new one in the content
            first_marker = content.find("---")
            second_marker = content.find("---", first_marker + 3)
            
            new_content = content[:first_marker + 3] + "\n" + new_header_content + "\n" + content[second_marker:]
            
            # Write the updated content back to the file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated title in {filepath}")
    except Exception as e:
        print(f"Error processing file {filepath}: {str(e)}")

def find_markdown_files(directory: str) -> List[str]:
    """
    Recursively find all .md files in the given directory
    """
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main():
    parser = argparse.ArgumentParser(description='Process markdown files to ensure title fields have double quotes')
    parser.add_argument('directory', type=str, help='Directory to recursively search for .md files')
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        sys.exit(1)
    
    markdown_files = find_markdown_files(args.directory)
    print(f"Found {len(markdown_files)} markdown files")
    
    for file in markdown_files:
        update_file_with_quoted_title(file)
    
    print("Processing complete")

if __name__ == "__main__":
    main()