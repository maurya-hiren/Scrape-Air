import PyPDF2
import pandas as pd

pdf_file_path = 'test.pdf'
output_file_path = 'output_combined3.txt'
excel_file_path = 'output_data3.xlsx'

# Extract text from PDF and combine into a single text file
with open(pdf_file_path, 'rb') as pdf_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Add a page header or separator
        output_file.write(f"=== Page {page_num + 1} ===\n")
        output_file.write(text + '\n')

# Read the combined text file and extract information into a DataFrame
data = []
with open(output_file_path, 'r', encoding='utf-8') as input_file:
    current_page = None
    current_product = {'Page': None, 'ProductID': None, 'ProductName': None, 'ItemSpecifics': None,
                       'Functions': None, 'HowToUse': None, 'PackageIncluding': None, 'Description': None}

    for line in input_file:
        line = line.strip()

        # Check if the line is a page header
        if line.startswith("=== Page ") and line.endswith(" ==="):
            current_page = int(line.split()[2])
        elif line and line[0].isdigit():
            # New product found based on lines starting with a numeric ID
            if current_product['Page'] is not None:
                data.append(current_product)
            current_product = {'Page': current_page, 'ProductID': line.split()[0], 'ProductName': line[len(line.split()[0]):].strip(),
                               'ItemSpecifics': None, 'Functions': None, 'HowToUse': None, 'PackageIncluding': None, 'Description': None}
        elif current_product['Page'] is not None:
            # Identify sections and update current product data
            if line.startswith("Item Specifics"):
                current_product['ItemSpecifics'] = line[len("Item Specifics: "):]
            elif line.startswith("Functions"):
                current_product['Functions'] = line[len("Functions: "):]
            elif line.startswith("How to use"):
                current_product['HowToUse'] = line[len("How to use "):]
            elif line.startswith("Package including"):
                current_product['PackageIncluding'] = line[len("Package including : "):]
            elif line.startswith("Description") or line.startswith("Product Description") or line.startswith("Introduction"):
                current_product['Description'] = line[len("Description: "):]

# Append the last product to the data list
if current_product['Page'] is not None:
    data.append(current_product)

# Convert the extracted data to a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Data extracted and saved to {excel_file_path}")
