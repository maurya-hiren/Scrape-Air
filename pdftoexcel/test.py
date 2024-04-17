import PyPDF2

pdf_file_path = './test.pdf'
output_file_path = 'output_combinednew.txt'

with open(pdf_file_path, 'rb') as pdf_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Add a page header or separator
        output_file.write(f"=== Page {page_num + 1} ===\n")
        output_file.write(text + '\n')

print(f"Text extracted and combined into {output_file_path}")
