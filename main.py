from PDFReader import PDFReader


file = "Amazon.pdf"
file_to_write = "order.csv"
if __name__ == '__main__':
    reader = PDFReader("Amazon.pdf",file_to_write)
    reader.open_pdf()