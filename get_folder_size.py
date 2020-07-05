# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:32:55 2020

@author: aswain
"""

import os
import argparse

database = {}
def dir_size(dirpath):
    total_size = 0
    for (path,dirs,files) in os.walk(dirpath):
        for file in files:
            total_size += os.path.getsize(os.path.join(path,file))
    return total_size/(1024*1024)
    
def print_all_dir_sizes(path):
    for (path,dirs,files) in os.walk(path):
        for dir in dirs:
            dirpath = os.path.join(path,dir)
            #print("Dir name {} --> Size {} MB\n".format(str(dir),dir_size(dirpath)))
            database[str(dir)] = dir_size(dirpath)
        break;
        
#print_all_dir_sizes(os.getcwd())
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path",type=str)
    args = parser.parse_args()
    print_all_dir_sizes(args.path)
    sorted_x = sorted(database.items(), key = lambda kv:kv[1],reverse=True)
    for k,v in sorted_x:
        print("Folder {} -- --> {} MB".format(k,v))
#print_all_dir_sizes("C:\\Users\\aswain\\OneDrive - Qualcomm\\Documents\\Python Scripts")