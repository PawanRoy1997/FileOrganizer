import os
import glob

files_in_current_dir = glob.glob('*')
file_extensions = set()

for file in files_in_current_dir:
    file_parts = file.split('.')
    try:
        file_extensions.add(file_parts[-1])
    except IndexError:
        continue

def create_directory():
    for extension in file_extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            continue
def arrangeFiles():
    for file in files_in_current_dir:
        fileExtension = file.split('.')[-1]
        try:
            os.rename(file,fileExtension+"/"+file)
        except (OSError, IndexError):
            continue

create_directory()
arrangeFiles()
print("Done!")

