import pandas as pd

# Read the Excel file
df = pd.read_excel('Sample.xlsx')

# Convert the DataFrame to a Markdown table
markdown_table = df.to_markdown(index=False)

# Save the Markdown table to a file
with open('output.md', 'w') as f:
    f.write(markdown_table)
