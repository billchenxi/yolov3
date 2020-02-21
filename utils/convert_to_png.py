""" Convert tiff image to png image
Author: Bill
Date: 2-21-2020
"""
import cv2
import os

data_path = "../J_data/Data_2_20"

tiff_images = [os.path.join(data_path, img) for img in os.listdir(data_path) if img.endswith(".tif")]

for img_path in tiff_images:
    img = cv2.imread(img_path, 1)
    # print(img.shape)
    cv2.imwrite(os.path.splitext(img_path)[0]+".png", img)
    img = cv2.imread(os.path.splitext(img_path)[0]+".png")
    # print(img.shape)