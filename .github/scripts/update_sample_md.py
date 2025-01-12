import sys
import os

# Check if the required arguments are provided
if len(sys.argv) < 4:
    raise ValueError("Usage: update_sample_md.py <table_file_path> <section_name> <target_file>")

table_file_path = sys.argv[1]
section_name = sys.argv[2]
target_file = sys.argv[3]

# Check if the table file exists
if not os.path.exists(table_file_path):
    raise FileNotFoundError(f"Table file not found: {table_file_path}")

# Read the table content from the file
with open(table_file_path, 'r') as f:
    markdown_table = f.read()

# Check if the target file exists
if not os.path.exists(target_file):
    raise FileNotFoundError(f"Target file not found: {target_file}")

# Read the existing content of the target file
with open(target_file, 'r') as f:
    content = f.readlines()

# Find the section starting with the specified section name
start_index = None
for i, line in enumerate(content):
    if line.strip() == section_name:
        start_index = i
        break

if start_index is not None:
    # Check if the next line starts with '|'
    if start_index + 1 < len(content) and content[start_index + 1].startswith('|'):
        # Find the end of the table
        end_index = start_index + 1
        while end_index < len(content) and content[end_index].startswith('|'):
            end_index += 1
        # Remove the existing table
        content = content[:start_index + 1] + content[end_index:]
    # Insert the new table
    content.insert(start_index + 1, markdown_table + '\n')
else:
    # If the section is not found throw an error
    raise ValueError(f"Section not found: {section_name}")

# Write the updated content back to the target file
with open(target_file, 'w') as f:
    f.writelines(content)
