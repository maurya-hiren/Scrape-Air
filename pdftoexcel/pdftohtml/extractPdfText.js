const fs = require('fs');
const pdf2json = require('pdf2json');

// Function to extract text content from a PDF file
function extractTextFromPDF(pdfPath) {
  const pdfParser = new pdf2json();

  // Register event handlers for pdfParser
  pdfParser.on('pdfParser_dataReady', pdfData => {
    if (pdfData && pdfData.formImage && pdfData.formImage.Pages) {
      // Access the text content
      const textContent = pdfData.formImage.Pages.reduce((acc, page) => {
        if (page && page.Texts) {
          page.Texts.forEach(text => {
            acc += Buffer.from(text.R[0].T, 'base64').toString('utf-8') + ' ';
          });
        }
        return acc;
      }, '');

      // Log the extracted text
      console.log("Extracted Text:", textContent);
    } else {
      console.error("Error: No valid data found in the PDF file.");
    }
  });

  pdfParser.on('pdfParser_dataError', error => {
    console.error("Error extracting text:", error);
  });

  // Read the PDF file and feed it to the pdfParser
  const pdfBuffer = fs.readFileSync(pdfPath);
  pdfParser.parseBuffer(pdfBuffer);
}

// Example usage
const pdfPath = './test.pdf';
extractTextFromPDF(pdfPath);
