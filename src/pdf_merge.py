'''
Created on 27 Apr 2022

@author: shalomshachne
'''
import os
from PyPDF2 import PdfFileMerger

# pass the path of the parent_folder
def fetch_all_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            target_files.append(os.path.join(path, name))
    return target_files 


def merge_pdf(out_path: str, extracted_files: list [str]):
    merger   = PdfFileMerger()
    
    for pdf in extracted_files:
        try:
            merger.append(pdf, import_bookmarks=False)
        except Exception as e:
            print(f'error merging={pdf}, ex={e}')

    merger.write(out_path)
    merger.close()
