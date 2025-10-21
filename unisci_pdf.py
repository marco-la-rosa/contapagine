import os
import sys
from pypdf import PdfWriter  # se usi pypdf
# from PyPDF2 import PdfMerger  # se usi PyPDF2

def merge_pdfs(pdf_list, output_path):
    writer = PdfWriter()
    for pdf_path in pdf_list:
        # verifica che termini in .pdf e che esista
        if not pdf_path.lower().endswith('.pdf'):
            print(f"Saltato (non PDF): {pdf_path}")
            continue
        if not os.path.isfile(pdf_path):
            print(f"File non trovato: {pdf_path}")
            continue

        # append all pages
        writer.append(pdf_path)
        print(f"Aggiunto: {pdf_path}")

    # scrivi output
    with open(output_path, 'wb') as out_f:
        writer.write(out_f)
    print(f"PDF unito scritto in: {output_path}")

def main():
    if len(sys.argv) < 3:
        print("Devi fare: python unisci_pdf.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        sys.exit(1)

    output_file = sys.argv[1]
    input_pdfs = sys.argv[2:]

    merge_pdfs(input_pdfs, output_file)

if __name__ == "__main__":
    main()
