# Import PyPDF2 library
from PyPDF2 import PdfReader, PdfWriter

# Print header
print("PDF Page Extractor")
print("==================\n")

# Get the PDF filename from user
filename = input("Enter the PDF filename: ")

# Open and read the PDF file
# (use PdfReader to open the PDF)
pdf_reader = PdfReader(filename)

# Get total number of pages
# (use len() on the pages)
total_pages = len(pdf_reader.pages)

# Display PDF information
print("PDF loaded successfully!")
print(f"Total pages in PDF: {total_pages}\n")

# Get page numbers from user
# (ask for comma-separated page numbers)
page_input = input("Enter page numbers to extract (comma-separated, e.g., 1,3,5): ")

# Convert the input string to a list of integers
# (split by comma, strip spaces, convert to int)
page_numbers = [int(page.strip()) for page in page_input.split(',')]

# Print extraction message
print(f"\nExtracting pages: {', '.join(map(str, page_numbers))}...\n")

# Create a PDF writer object
# (use PdfWriter to create new PDF)
pdf_writer = PdfWriter()

# Extract and add pages to the new PDF
# (loop through the page numbers)
# (remember: PDF pages are 0-indexed, so subtract 1)
for page_num in page_numbers:
    pdf_writer.add_page(pdf_reader.pages[page_num - 1])

# Save the new PDF file
# (open a file in write-binary mode and use .write())
output_filename = "extracted_pages.pdf"
with open(output_filename, 'wb') as output_file:
    pdf_writer.write(output_file)

# Print success messages
print("Pages extracted successfully!")
print(f"New PDF saved as: {output_filename}\n")
print("Extraction complete!")