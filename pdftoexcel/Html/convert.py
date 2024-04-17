import pdfkit

# Read the PDF file
pdf_file = open('test.pdf', 'rb')

# Convert the PDF to HTML
pdf_to_html = pdfkit.from_file(pdf_file, output_path='my_html_file.html', options={'quiet': ''})

# Close the PDF file
pdf_file.close()