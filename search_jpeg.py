import os
import zipfile

directory = "/random_files"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

sig = b'\xFF\xD8'

def is_jpeg(file):
    try:
        with open(file, 'rb') as f:
            return f.read(2) == sig
    except Exception:
        return False


for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath) and is_jpeg(filepath):
        new_filename = filename + ".jpg"
        new_filepath = os.path.join(directory, new_filename)

        os.rename(filepath, new_filepath)
        print(f"Renamed: {filename} -> {new_filename}")
    else:
        os.remove(filepath)
        print(f"Deleted: {filename}")
