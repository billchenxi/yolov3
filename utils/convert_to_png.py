""" Convert tiff image to png image
Author: Bill
Date: 2-21-2020
"""
import cv2
import os
import argparse


parser = argparse.ArgumentParser(description='Convert tiff to png')
parser.add_argument('--dataset_path', type=str, help='path to the png')
parser.add_argument('--output_path', type=str, help='output path')
parser.add_argument('--image_type', type=str, help='jpg or png', default='.png')

args = parser.parse_args()

def main(args):
    dat_path = args.dataset_path
    out_path = args.output_path
    img_type = args.image_type

    tiff_images = [os.path.join(dat_path, img) for img in os.listdir(dat_path) if img.endswith(".tif")]

    # Progress bar
    progress_length = len(data)
    progress_cnt = 0
    printProgressBar(0, progress_length, prefix='\nVOC Generate:'.ljust(15), suffix='Complete', length=40)



    for img_path in tiff_images:
        img = cv2.imread(img_path, 1)
        # print(img.shape)
        cv2.imwrite(os.path.join(out_path, \
                    os.path.splitext(img_path)[0]+img_type, img))
        printProgressBar(progress_cnt + 1, progress_length, prefix='Converting images:'.ljust(15), suffix='Complete', length=40)
        progress_cnt += 1

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s|%s| %s%% (%s/%s)  %s' % (prefix, bar, percent, iteration, total, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print("\n")

if __name__ == '__main__':
    main(args)