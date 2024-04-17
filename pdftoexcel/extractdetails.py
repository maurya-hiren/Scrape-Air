import re
import json

def extract_product_details(text):
    # Regular expression pattern for product headers
    product_pattern = re.compile(r"\d{3} -.*$", re.MULTILINE)

    # Find all product headers
    product_headers = product_pattern.findall(text)

    # Split the text into sections based on these headers
    product_sections = product_pattern.split(text)[1:]  # Skip the first split part

    # Dictionary to hold the product details
    products = {}

    for header, section in zip(product_headers, product_sections):
        # Process 'section' to extract relevant details
        # This could involve further regex matching or string processing
        # For now, we will just store the entire section
        products[header] = section.strip()

    return products

# Read the text file content
with open('output_combinednew.txt', 'r', encoding='utf-8') as file:
    text_content = file.read()

# Extract product details
product_details = extract_product_details(text_content)

# Convert to JSON
json_output = json.dumps(product_details, indent=4)

# Write to a JSON file
with open('output_json_file.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)
