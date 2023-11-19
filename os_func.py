import os
import shutil
import datetime
import csv
import json
import re

# copy, move, rename, delete
# create directory, change
# dest_dir="D:\\Python_Training\\new_dir"
#
# if not os.path.exists(dest_dir):
#     os.mkdir(dest_dir)
#
# file_path="C:\\Users\\Latitude\\PycharmProjects\\Python-Training\\inventory.txt"
# shutil.copy(file_path, dest_dir)
#
# os.remove(os.path.join(dest_dir, 'new_inventory.txt'))
# # os.rename(os.path.join(dest_dir, 'inventory.txt'), os.path.join(dest_dir, 'new_inventory.txt'))
#
# nest_dir="D:\\Python_Training\\new_dir\\test1\\test2"
# os.makedirs(nest_dir, exist_ok=True)

print(os.getcwd())
new_path=os.path.join("C:\\",'Users', 'Latitude', 'Documents')
os.chdir(new_path)
print(os.getcwd())
