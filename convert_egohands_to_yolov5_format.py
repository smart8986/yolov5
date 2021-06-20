#-*- coding:utf-8

import os
import pandas as pd

src_files = ['./images/train/train_labels.csv', './images/test/test_labels.csv']
dst_dir = ['./labels/train/', './labels/test/']

def convert(src_file, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    data = pd.read_csv(src_file, encoding='utf-8')
    for line in data.values:
        # filename	width	height	class	xmin	ymin	xmax	ymax
        filename, width, height, class_hand, xmin, ymin, xmax, ymax = line
        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        w_hand = (xmax - xmin) / width
        h_hand = (ymax - ymin) / height
        with open(dst_dir + filename[:-3]+'txt','a') as f1:
            f1.write("0 %f %f %f %f\n" % (x_center, y_center, w_hand, h_hand))

convert(src_files[0], dst_dir[0])
convert(src_files[1], dst_dir[1])

