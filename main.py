#!/usr/bin/env python3               

"""                     
python directory size checker /path/to/directory
Total size: 2.5 GB          

"""                            

import sys                        
import os

loc = sys.argv[1]
files = os.listdir(loc)
size = 0

for x in files:
    file_path = os.path.join(loc, x)
    file_size = os.path.getsize(file_path)
    size += file_size

total_size = round(size / (1024*1024), 3)

if __name__ == '__main__':
    try:
        print(f'Total size: {total_size} GB')

    except FileNotFoundError:
        print('error')
