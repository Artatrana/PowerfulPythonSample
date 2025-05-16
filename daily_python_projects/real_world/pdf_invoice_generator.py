# Project Description
# In today’s project we will create a command-line tool that generates PDF invoices for customers.
# The user provides customer information, purchased items, and prices through a JSON input file.
# The tool calculates totals, applies taxes, and saves the invoice as a professional-looking PDF document.
# Here is how the generated PDF will look like:

from fpdf import FPDF
import json

class InvoicePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Invoice", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_business_info(self, business_name, business_address):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, business_name, ln=True)
        self.set_font("Arial", "B", 12)
        self.multi_cell(0, 10, business_address)

    def add_customer_info(self, customer_name, customer_address):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"Bill To: {customer_name}", ln=True)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, customer_address)

    def add_table_header(self):
        self.set_font("Arial", "B", 10)
        self.cell(80, 10, "Description", border=1)
        self.cell(30, 10, "Quantity", border=1, align="C")
        self.cell(40, 10, "Unit Price", border=1, align="C")
        self.cell(40, 10, "Total", border=1, align="C")
        self.ln()
    def add_table_row(self, description, quantity, unit_price, total):
        self.set_font("Arial", "", 10)
        self.cell(80, 10, description, border=1)
        self.cell(30, 10, str(quantity), border=1, align="C")
        self.cell(40, 10, f"${unit_price:.2f}", border=1, align="C")
        self.cell(40, 10, f"${total:.2f}", border=1, align="C")
        self.ln()

    def add_totals(self, subtotal, tax, total):
        self.set_font("Arial", "B", 10)
        self.cell(150, 10, "Subtotal", border=1, align="R")
        self.cell(40, 10, f"${subtotal:.2f}", border=1, align="C")
        self.ln()
        self.cell(150, 10, "Tax", border=1, align="R")
        self.cell(40, 10, f"${tax:.2f}", border=1, align="C")
        self.ln()
        self.cell(150, 10, "Total", border=1, align="R")
        self.cell(40, 10, f"${total:.2f}", border=1, align="C")

def generate_invoice(data_file, output_file):
    with open(data_file, "r") as file:
        data = json.load(file)

    pdf = InvoicePDF()
    pdf.add_page()

    # Add business and customer info
    pdf.add_business_info(data["business_name"], data["business_address"])
    pdf.ln(10)
    pdf.add_customer_info(data["customer_name"], data["customer_address"])
    pdf.ln(10)

    # Add table with items
    pdf.add_table_header()
    subtotal = 0
    for item in data["items"]:
        total = item["quantity"] * item["unit_price"]
        subtotal += total
        pdf.add_table_row(item["description"], item["quantity"], item["unit_price"], total)

    # Add totals
    tax = subtotal * data["tax_rate"]
    total = subtotal + tax
    pdf.ln(5)
    pdf.add_totals(subtotal, tax, total)

    # Output PDF
    pdf.output(output_file)
    print(f"Invoice saved to {output_file}")

if __name__ == "__main__":
    generate_invoice("invoice_data.json", "invoice.pdf")
