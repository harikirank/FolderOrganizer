import os
import pathlib
from typing import List

image_extensions = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp']


def is_desired_file_type(file, desired_file_types: List[str]):
    return pathlib.Path(file).suffix in desired_file_types


def create_folder_if_not_exists(base_folder, sub_folder):
    os.path.isdir(f"{base_folder}/{sub_folder}") or os.mkdir(f"{base_folder}/{sub_folder}")


def group_image_files(folder='./Desktop'):
    base_folder = folder
    images_folder = 'images'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, image_extensions):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=images_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{images_folder}/{file}")


def group_pdf_files(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'pdfs'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, [".pdf"]):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_text_files(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'texts'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, [".txt"]):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_excel_and_csv_files(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'excel_and_csvs'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, ['.xls', '.xlsx', '.csv']):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_docxs(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'docxs'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, ['.doc', '.docx']):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_shortcuts(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'shortcuts'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, ['.lnk']):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_py_ipynbs(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'py_ipynbs'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, ['.py', '.ipynb']):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


def group_executables(folder='./Desktop'):
    base_folder = folder
    pdf_folder = 'executables'

    all_files = os.listdir(folder)
    for file in all_files:
        if is_desired_file_type(file, ['.exe', '.msi']):
            create_folder_if_not_exists(base_folder=base_folder, sub_folder=pdf_folder)
            os.rename(f"{folder}/{file}", f"{base_folder}/{pdf_folder}/{file}")


if __name__ == "__main__":
    # group_image_files()
    # group_pdf_files()
    # group_text_files()
    # group_excel_and_csv_files()
    # group_docxs()
    group_shortcuts()
    group_py_ipynbs()
    group_executables()
    print(os.listdir("./Desktop"))
