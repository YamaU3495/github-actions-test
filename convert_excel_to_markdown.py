import pandas as pd
import sys

# Check if the Excel file path is provided as a command-line argument
if len(sys.argv) < 2:
    raise ValueError("Excel file path must be provided as a command-line argument")

# Get the Excel file path from the command-line arguments
excel_file_path = sys.argv[1]

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Convert the DataFrame to a Markdown table
markdown_table = df.to_markdown(index=False)

# Print the Markdown table
sys.stdout.write(markdown_table)