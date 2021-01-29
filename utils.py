from PIL import Image
from PyPDF2 import PdfFileMerger

def image_to_pdf(path_file):
    img = Image.open(path_file)
    img = img.convert('RGB')
    file_name = path_file.split('/')[-1]
    new_path = f"results/{file_name.split('.')[0]}.pdf"
    img.save(new_path)
    return new_path

def pdf_merge(input_files):
    merger = PdfFileMerger()
    for pdf in input_files: merger.append(pdf)
    merger.write("results/pdf_merged_result.pdf")
    merger.close()
