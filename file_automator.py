import os
import pathlib
from typing import List


def group_files(folder_to_look, sub_folder_to_store_grouped_files, file_extensions_to_group):
    all_files = os.listdir(folder_to_look)
    for file in all_files:
        if is_desired_file_type(file, file_extensions_to_group):
            create_folder_if_not_exists(folder_to_look=folder_to_look,
                                        sub_folder_to_store_grouped_files=sub_folder_to_store_grouped_files)
            os.rename(f"{folder_to_look}/{file}", f"{folder_to_look}/{sub_folder_to_store_grouped_files}/{file}")


def create_folder_if_not_exists(folder_to_look, sub_folder_to_store_grouped_files):
    os.path.isdir(f"{folder_to_look}/{sub_folder_to_store_grouped_files}") or os.mkdir(
        f"{folder_to_look}/{sub_folder_to_store_grouped_files}")


def is_desired_file_type(file, desired_file_types: List[str]):
    return pathlib.Path(file).suffix in desired_file_types


if __name__ == "__main__":
    base_folder = "./Desktop"  # change this depending on the location

    sub_folder = 'Images'
    extensions = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'PDFs'
    extensions = [".pdf"]
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Texts'
    extensions = [".txt"]
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Excel_and_CSVs'
    extensions = ['.xls', '.xlsx', '.csv']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Word Docs'
    extensions = ['.doc', '.docx']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Shortcuts'
    extensions = ['.lnk']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Py_IPYNBs'
    extensions = ['.py', '.ipynb']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Executables'
    extensions = ['.exe', '.msi']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Tableau Workbooks'
    extensions = ['.twb']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'Log Files'
    extensions = ['.log']
    group_files(base_folder, sub_folder, extensions)

    sub_folder = 'SSH Key Pairs'
    extensions = ['.pem']
    group_files(base_folder, sub_folder, extensions)
