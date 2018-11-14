
import shutil
import sys
import os

input_txt = sys.argv[1]
src_folder = sys.argv[2]
output_folder = sys.argv[3]

if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)

os.mkdir(output_folder)

with open(input_txt, 'r') as f:
    files = f.readlines()
    for file in file:
        folder = files[: -11]
        shutil.copy(os.path.join(src_folder, folder, file), os.path.join(output_folder, file))
