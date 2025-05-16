from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader, PdfWriter

def file_merge():
    merger = PdfMerger()
    merger.append("pdf_file/Artatrana_Cuberg_H1B.pdf")
    merger.append("pdf_file/I-94_Artatrana.pdf")
    merger.append("pdf_file/Artatrana_H4_EAD_Application_receipt.pdf")
    merger.write("pdf_file/Artatrana_Cuberg_H1_I94_H4.pdf")
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
    input_pdf = "pdf_file/Artatrana_Mca_Bsc.pdf"
    output_folder = "pdf_file/split_pages"
    #split_pdf2(input_pdf, output_folder)
    file_merge()

