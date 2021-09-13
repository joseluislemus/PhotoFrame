# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:26:45 2021

@author: Josel
"""

import glob 

#global vars
delay_seconds = 20
photos_directory = "./PhotoFrame"
randomize = True
image_files = glob.glob(photos_directory + '/**/*.jpg', recursive = True)
nav_next = False
nav_previous = False