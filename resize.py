import numpy as np
import math
import os
import argparse
from PIL import Image, ImageOps

def img_to_square(img):
    w, h = img.size
    padding_right = 0
    padding_bottom = 0
    if w % 32 != 0:
        new_w = math.ceil(w /32) * 32
        padding_right = new_w - w
        padding_bottom = new_w - h
    else:
        padding_bottom = w - h

    border = (0, 0, padding_right, padding_bottom)
    # new_img =cv2.copyMakeBorder(img, 0 , padding_bottom, 0, padding_right, cv2.BORDER_CONSTANT, value=[0,0,0])
    new_img = ImageOps.expand(img, border=border,fill='black')
    return new_img

def img_to_32_multiplier(img):
    
    w, h= img.size
    padding_right = 0
    padding_bottom = 0
    if w % 32 != 0:
        new_w = math.ceil(w /32) * 32
        padding_right = new_w - w
    if h % 32 != 0:
        new_h = math.ceil(h /32) * 32
        padding_bottom = new_h - h
    border = (0, 0, padding_right, padding_bottom)
    # new_img = cv2.copyMakeBorder(img, 0 , padding_bottom, 0, padding_right, cv2.BORDER_CONSTANT, value=[0,0,0])
    new_img = ImageOps.expand(img, border=border,fill='black')
    return new_img

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', '-m', type=str, default='m32', help='resize method m32/squared')
    parser.add_argument('--src_path', '-sp', type=str, help='folder path to source images')
    parser.add_argument('--output_path', '-op', type=str, default='.', help='folder path to output images')
    opt = parser.parse_args()


    included_extention = ('jpg', 'bmp', 'png', 'gif')
    img_list = [ img for img in os.listdir(opt.src_path) if img.endswith(included_extention)]

    for img_name in img_list:
        # img = cv2.imread(os.path.join(opt.src_path, img_name))
        img = Image.open(os.path.join(opt.src_path, img_name))
        if opt.method == "m32":
            new_path = os.path.join(opt.output_path,img_name.split(".")[0] + "_m32.jpg")
            new_img = img_to_32_multiplier(img)
            # cv2.imwrite(new_path, new_img)
            new_img.save(new_path)
            print("Save images to {}".format(new_path))
        else:
            new_path = os.path.join(opt.output_path,img_name.split(".")[0] + "_squared.jpg")
            new_img = img_to_square(img)
            # cv2.imwrite(new_path, new_img)
            new_img.save(new_path)
            print("Save images to {}".format(new_path))

    
        