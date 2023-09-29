#"C:\Users\USER\Downloads\life_ex _g.xlsx"
import openpyxl
import csv

# Specify the path to your XLSX file
xlsx_file_path = r"C:\Users\USER\Desktop\Life_Project\Hosp_Amount\data\Hosp_Amount.xlsx"

# Specify the path where you want to save the CSV file
csv_file_path = r'C:\Users\USER\Desktop\Life_Project\Hosp_Amount\data\Hosp_first.csv'

# Open the XLSX file for reading
workbook = openpyxl.load_workbook(xlsx_file_path, data_only=True)

# Select the first sheet in the workbook
sheet = workbook.active

# Extract the header row (first row in the sheet)
header = [cell.value for cell in sheet[1]]

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the extracted header row to the CSV file
    csv_writer.writerow(header)
    
    # Iterate through rows in the sheet starting from the second row (index 1)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        csv_writer.writerow(row)