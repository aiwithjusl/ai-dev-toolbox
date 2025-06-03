# devtoolbox/utils/io_helpers.py

def read_txt(file_path):
    """Reads and returns the content of a .txt file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
