from pathlib import Path
from shutil import copy
import os

l = []
parent = input("Enter parent directory path: ")
for filename in Path(parent).glob('**/*'):
    s = str(filename)
    if s[len(s)-4:len(s)] == '.jpg':
        l.append(s)
print(l)
folder_name = input("Enter folder name: ")
os.mkdir('/Users/chale/Desktop/'+folder_name)
for x in l:
    copy(x, '/Users/chale/Desktop/'+folder_name)

