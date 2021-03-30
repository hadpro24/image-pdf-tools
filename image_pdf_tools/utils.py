import os
from datetime import datetime

from PIL import Image
from PyPDF2 import PdfFileMerger

def is_path_exist(path: str, folder: bool=True) -> bool:
    is_exist = os.path.isdir(path) if folder else os.path.isfile(path)
    if not is_exist: 
        print(f'[ERROR]: The path {path} specified does not exist')
        return False
    return True

def image_to_pdf(path_file: str, folder_save: str) -> bool:
    """
        Image to pdf converter
    """

    # testing file exist
    if not is_path_exist(path_file, False):
        return False

    # Open file and save it it new folder
    img = Image.open(path_file)
    img = img.convert('RGB')
    file_name = path_file.split('/')[-1]

    # convert file
    new_path = f"{file_name.split('.')[0]}_{datetime.now()}.pdf"
    if not is_path_exist(folder_save):
        return False

    # save file
    img.save('{}/{}'.format(folder_save, new_path))
    return True

def pdf_merge(path_files: list, folder_save: str):
    """
        PDF merge
    """
    if not isinstance(path_files, list):
        return False
    for path in path_files:
        if not is_path_exist(path, False):
            return False

    # merging pdf with pdffilemanager  
    merger = PdfFileMerger(strict=False)
    for pdf in path_files:
        merger.append(pdf)

    # save file
    new_path = f"merged_{datetime.now()}.pdf"
    if not is_path_exist(folder_save):
        merger.close()
        return False
    merger.write("{}/{}".format(folder_save, new_path))
    merger.close()
    return True
