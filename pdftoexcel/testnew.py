import json
import re

def convert_to_json_with_dynamic_products(file_path):
    pages_data = []
    page_content = ''
    current_page_number = 1

    # Regular expression pattern to identify product names
    product_pattern = re.compile(r'^\d+ -.*$')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip().startswith('=== Page'):
                if page_content:
                    # Process the previous page
                    add_page_data(pages_data, page_content, current_page_number, product_pattern)
                    page_content = ''  # Reset page content
                current_page_number = int(line.strip().split(' ')[2])  # Update page number
            else:
                page_content += line

        # Add the last page
        if page_content:
            add_page_data(pages_data, page_content, current_page_number, product_pattern)

    # Convert list to JSON
    return json.dumps({"pages": pages_data}, indent=4)

def add_page_data(pages_data, content, page_number, product_pattern):
    # Find products in the content
    products_in_page = product_pattern.findall(content)
    page_data = {
        "page_number": page_number,
        "content": content.strip()
    }
    if products_in_page:
        page_data["products"] = products_in_page
    pages_data.append(page_data)

# File path to the text document
file_path = './output_combinednew.txt'  # Replace with your file path

# Convert the text file to JSON
json_data = convert_to_json_with_dynamic_products(file_path)

# Output the JSON data
print(json_data)
