# !/usr/bin/python

import os
import glob
files = glob.glob('*.svg')
for file in files:
    os.rename(file, file[1:])

# for file in files:
#     parts = file.split('_') #[abc, 2000.jpg]
#     new_name = 'year_{}'.format(parts[1]) #year_2000.jpg
#     os.rename(file, new_name)
