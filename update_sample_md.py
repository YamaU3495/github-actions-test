import sys
import os

# Check if the table file path is provided as a command-line argument
if len(sys.argv) < 2:
    raise ValueError("Table file path must be provided as a command-line argument")

table_file_path = sys.argv[1]

# Check if the table file exists
if not os.path.exists(table_file_path):
    raise FileNotFoundError(f"Table file not found: {table_file_path}")

# Read the table content from the file
with open(table_file_path, 'r') as f:
    markdown_table = f.read()
    print(markdown_table)

# Check if Sample.md exists
if not os.path.exists('Sample.md'):
    raise FileNotFoundError("Sample.md not found")

# Read the existing content of Sample.md
with open('Sample.md', 'r') as f:
    content = f.readlines()

# Find the section starting with '# Sample.md'
start_index = None
for i, line in enumerate(content):
    if line.strip() == '# Sample.md':
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
    # If the section is not found, append the new table at the end
    content.append('# Sample.md\n')
    content.append(markdown_table + '\n')

# Write the updated content back to Sample.md
with open('Sample.md', 'w') as f:
    f.writelines(content)
