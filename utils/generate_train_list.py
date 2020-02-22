""" Convert tiff image to png image
Author: Bill
Date: 2-21-2020
"""
import cv2
import os
import argparse
import math
from random import sample 

parser = argparse.ArgumentParser(description='Generate Training List')
parser.add_argument('--dataset_path', type=str, help='path to the png')
parser.add_argument('--percentage', type=int, help='percentage of the data will be in training')
parser.add_argument('--output_path', type=str, help='output path for train on different machine')
parser.add_argument('--save_path', type=str, help='where the train list file save to')


args = parser.parse_args()

def main(args):
    dat_path = args.dataset_path
    out_path = args.output_path
    training_split = args.percentage
    save_path = args.save_path

    img_list = [os.path.join(dat_path, img) for img in os.listdir(dat_path)]
    train_list = sample(img_list, math.floor(len(img_list)*(training_split/100)))
    
    # Progress bar ---------------------
    progress_length = len(train_list)
    progress_cnt = 0
    printProgressBar(0, progress_length, prefix='\nTrain'.ljust(15), suffix='Complete', length=40)
    # Progress bar end ---------------------

    with open(save_path+"train.txt", 'w') as out_file:
        for img_path in train_list:
            output_row = os.path.join(out_path, os.path.basename(img_path))
            out_file.write(output_row + "\n")
            
            printProgressBar(progress_cnt + 1, progress_length, prefix='Converting images:'.ljust(15), suffix='Complete', length=40)
            progress_cnt += 1
    
    val_list = [elem for elem in img_list if elem not in train_list]
    # Progress bar ---------------------
    progress_length = len(val_list)
    progress_cnt = 0
    printProgressBar(0, progress_length, prefix='\nTrain'.ljust(15), suffix='Complete', length=40)
    # Progress bar end ---------------------

    with open(save_path+"val.txt", 'w') as out_file:
        for img_path in val_list:
            output_row = os.path.join(out_path, os.path.basename(img_path))
            out_file.write(output_row + "\n")
            
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