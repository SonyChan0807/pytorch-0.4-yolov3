import os
import sys
import shutil

if __name__ == "__main__":
    
    if len(sys.argv) == 4:
    
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        interval  = int(sys.argv[3])

        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)    
        os.mkdir(output_folder)

        dirs = sorted([f.path for f in os.scandir(input_folder) if f.is_dir()])
        for d in dirs:
            files = sorted(os.listdir(d))
            for idx, file in enumerate(files):
                if idx % interval == 0:
                    shutil.copyfile(os.path.join(d,file), os.path.join(output_folder, file)) 
    else:
        print('Usage: ')
        print('  python gen_sample.py input_dir output_dir sample_interval')

