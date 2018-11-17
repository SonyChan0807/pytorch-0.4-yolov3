import os
import sys
import shutil

if __name__ == "__main__":
    
    input_folder = "images/Echabdens_Route_de_la_Gare_4"
    output_folder = "Ech_4_sample"
    interval = 50
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)    
    os.mkdir(output_folder)


    files = sorted(os.listdir(output_folder))
    for idx, file in enumerate(files):
        if idx % interval == 0:
            shutil.copyfile(os.path.join(input_folder,file), os.path.join(output_folder, file)) 
