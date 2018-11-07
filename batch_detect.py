import sys
import time
from PIL import Image, ImageDraw
import cv2
import os
import argparse

from utils import *
from image import letterbox_image, correct_yolo_boxes
from darknet import Darknet
from resize import img_to_32_multiplier



namesfile=None
def detect(m,img, img_name, use_cuda):    
    sized = letterbox_image(img, m.width, m.height)
    start = time.time()
    boxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
    correct_yolo_boxes(boxes, img.width, img.height, m.width, m.height)
    finish = time.time()
    print('%s: Predicted in %f seconds.' % (img_name, (finish-start)))
    return boxes


def detect_cv2(m, img, img_path, use_cuda):
    sized = cv2.resize(img, (m.width, m.height))
    sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)
    
    for i in range(2):
        start = time.time()
        boxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
        finish = time.time()
        if i == 1:
            print('%s: Predicted in %f seconds.' % (img_path, (finish-start)))
    return boxes
    
def model(cfg_file, weight_file):
    m = Darknet(cfg_file)
    m.print_network()
    m.load_weights(weight_file)
    print('Loading weights from %s... Done!' % (weight_file))

    return m


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', '-w', type=str, help='path of the trained weights')
    parser.add_argument('--cfg', '-c', type=str, help='path of yolo cfg file')
    parser.add_argument('--names', '-n', type=str, help='path of class names')
    parser.add_argument('--src_path', '-sp', type=str, help='folder path to source images')
    parser.add_argument('--output_path', '-op', type=str, default='.', help='folder path to output images')
    opt = parser.parse_args()
    

    globals()["namesfile"] = opt.names
    class_names = load_class_names(namesfile)

    model = model(opt.cfg, opt.weights)
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        m.cuda()

    included_extention = ('jpg', 'bmp', 'png', 'gif')
    img_generator = (img for img in os.listdir(opt.src_path) if img.endswith(included_extention))

    if not os.path.isdir(opt.output_path):
        os.mkdir(opt.output_path);

    for img_path in img_generator:
        print(img_path)
        # img = cv2.imread(os.path.join(opt.src_path,img_path))
        img = Image.open(os.path.join(opt.src_path,img_path)).convert('RGB')
        # img = img_to_32_multiplier(img)
        boxes = detect(model, img, img_path, use_cuda)
        # boxes = detect_cv2(model, img, img_path, use_cuda)
        # plot_boxes_cv2(img, boxes, os.path.join(opt.output_path,img_path), class_names)

        plot_boxes(img, boxes, os.path.join(opt.output_path,img_path.split(".")[0] + "_pil." + img_path.split(".")[1]), class_names)


