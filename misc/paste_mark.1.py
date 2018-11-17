from PIL import Image, ImageDraw
import os
import sys
import cv2
import numpy as np



def get_mask_3(mask):
    mask_img[mask_img < 255] = 1
    mask_img[mask_img == 255] = 0
    mask_img[mask_img == 1] = 255
    new_mask = np.expand_dims(mask_img, axis=2)
    mask_3 = np.concatenate((new_mask, new_mask,new_mask), axis=2)
    return mask_3

def put_mask(img, mask):
    h, w, d = img.shape
    mask_boolean = mask_3 == 255
    for i in range(0, h):
        for j in range(0, w):
            # print(mask_3.shape)
            # print(mask_3[i][j][0])
            if mask_3[i][j][0]:
                black = np.array([0,0,0])
                img[i][j] = black

if __name__ == "__main__":

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]


    files = os.listdir(input_folder)

    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    masks= [file for file in files if file.endswith("_mask.jpg")]
    img_paths = [file for file in files if file.endswith("_m32.jpg")]
    print(img_paths[:5])

    for img_path in img_paths:
        mask = img_path[:-15] + "_mask.jpg"
        print(img_path)
        print(mask)
        img = cv2.imread(os.path.join(input_folder, img_path), -1)
        mask_img = cv2.imread(os.path.join(input_folder, mask), 0)
        mask_3 =  get_mask_3(mask_img)
        put_mask(img, mask_3)
        cv2.imwrite(os.path.join(output_folder, img_path), img)
    

    

