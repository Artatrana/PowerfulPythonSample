from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader, PdfWriter

def file_merge():
    merger = PdfMerger()
    merger.append("pdf_file/split_pages/page_1.pdf")
    merger.append("pdf_file/split_pages/page_2.pdf")
    #merger.append("pdf_file/Artatrana_H4_EAD_Application_receipt.pdf")
    merger.write("pdf_file/H1B_Mphasis_Artatrana.pdf")
    merger.close()

def split_pdf2(input_pdf, output_folder):
    reader = PdfReader(input_pdf)

    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        output_path = f"{output_folder}/page_{page_num + 1}.pdf"
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)

    print("PDF split successfully.")

if __name__ == "__main__":
    input_pdf = "pdf_file/eStmt_2025-05-15.pdf"
    output_folder = "pdf_file/split_pages"
    split_pdf2(input_pdf, output_folder)
    #file_merge()

