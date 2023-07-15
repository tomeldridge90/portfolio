import pandas as pd
from openpyxl import load_workbook

# Read data from CSV file using pandas
data = pd.read_csv('data.csv')

# Define your spreadsheet template path
template_path = 'spreadsheet_template.xlsx'

# Load workbook
book = load_workbook(template_path)

# Select the active worksheet
sheet = book.active

# Suppose you want to write data into cells B2 to B4
sheet['B2'] = data.iloc[0,0]  # Write the first value from the first column of the CSV to B2
sheet['B3'] = data.iloc[1,0]  # Write the second value from the first column of the CSV to B3
sheet['B4'] = data.iloc[2,0]  # Write the third value from the first column of the CSV to B4

# Save the changes
book.save(template_path)
