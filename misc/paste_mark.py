from PIL import Image, ImageDraw
import os
import sys


input_folder = sys.argv[1]
output_folder = sys.argv[2]

files = os.listdir(input_folder)

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

# masks= [file for file in files if file.endswith(".png")]
img_paths = [file for file in files if file.endswith(".jpg")]
print(img_paths[:5])

for img_path in img_paths:
    mask = img_path[:-15] + ".png"
    
    print(img_path)
    print(mask)
    img = Image.open(os.path.join(input_folder, img_path))
    bg = Image.new("RGB", img.size,(255,255,255,255))
    bg.paste(img,(0,0))
    bg.save(os.path.join(output_folder, img_path.replace(".jpg", ".png")))
    
    # img.show()
    # draw = ImageDraw.Draw(img)
    # mask_img = Image.open(os.path.join(input_folder, mask))
    # mask_img.show()

    # x, y = mask_img.size
    # img.paste(mask_img)

    # # del draw
    # # img.save(os.path.join(output_folder, img_path))

    # print(img.size)
    # img.show()

    

