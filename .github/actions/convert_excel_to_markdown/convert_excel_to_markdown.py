import pandas as pd
import sys

# Check if the Excel file path is provided as a command-line argument
if len(sys.argv) < 2:
    raise ValueError("Usage: convert_excel_to_markdown.py <excel_file_path> [sheet_name]")

# Get the Excel file path from the command-line arguments
excel_file_path = sys.argv[1]

# Get the sheet name from the command-line arguments, if provided
sheet_name = sys.argv[2] if len(sys.argv) > 2 else None

# Read the Excel file
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Convert the DataFrame to a Markdown table
markdown_table = df.to_markdown(index=False)

# Print the Markdown table
sys.stdout.write(markdown_table)
