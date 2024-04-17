from pdf2docx import Converter

# Path to the PDF file
pdf_file = 'test.pdf'

# Output HTML file path
html_file = 'test.html'

# Convert PDF to HTML
cv = Converter(pdf_file)
cv.convert(html_file, start=0, end=None)
cv.close()

print(f"Conversion completed. The HTML file is saved as '{html_file}'")
