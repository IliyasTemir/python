#1
import os
from pathlib import Path

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

if __name__ == "__main__":
    path = input()

    if not os.path.exists(path):
        print("The specified path does not exist.")
    else:
        print("\nDirectories:", list_directories(path))
        print("Files:", list_files(path))
        print("All:", list_all(path))


#2
def check_path_access(path):
    return {
        "Existince": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }

#3
import os

def path_e(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return "Path does not exist"


#4
import os
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)
    
#5
def write_list(filename, data_list):
    with open(filename, 'w') as f:
        f.write("\n".join(data_list) + "\n")

#6
import string

def create_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{filename}\n")
        print(f"{filename}")

if __name__ == "__main__":
    create_text_files()
    
#7
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
        dest.write(src.read())
    print(f"'{source}''{destination}'")
    
if __name__ == "__main__":
    src_file = input()
    dest_file = input()
    copy_file(src_file, dest_file)

#8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return "Successfully deleted: {path}"
    return "No permission to delete"