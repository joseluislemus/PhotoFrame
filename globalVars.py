# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:26:45 2021

@author: Josel
"""

import glob 
from datetime import datetime
import pandas as pd
from PIL import Image,ExifTags


#global vars
delay_seconds = 10
delay_seconds_min = 5
delay_seconds_max = 1800

photos_directory = "./PhotoFrame"
allowed_photos_directory = glob.glob(photos_directory + '/**/', recursive = True)
image_files = glob.glob(photos_directory + '/**/*.jpg', recursive = True)

start_date = datetime.strptime('1970:01:01:00:00', '%Y:%m:%d:%H:%M')
end_date = datetime.strptime('2050:01:01:00:00', '%Y:%m:%d:%H:%M')

next_image = ''
current_image = ''

randomize = True

nav_next = False
nav_previous = False


image_df = pd.DataFrame(columns=['date','filename','speed','aperture','iso','focallength','camera'])
for image_file in image_files:
    image_dict = {}
    image_dict['filename'] = image_file
    image = Image.open(image_file)
    exif_data = {
                ExifTags.TAGS[k]: v
                for k, v in image._getexif().items()
                if k in ExifTags.TAGS
                }
    image_dict['date'] = exif_data['DateTimeDigitized']
    image_dict['speed'] = str(exif_data['ExposureTime'][0]) + '/' + str(exif_data['ExposureTime'][1])+'s'
    image_dict['aperture'] = 'F'+str(exif_data['FNumber'][0] / exif_data['FNumber'][1])
    image_dict['focallength'] = str(int(exif_data['FocalLength'][0] / exif_data['FocalLength'][1]))+'mm'
    image_dict['iso'] = str(exif_data['ISOSpeedRatings'])
    
    if exif_data['Make'] in exif_data['Model']:
        image_dict['camera'] = (exif_data['Model']).upper()
    else:
        image_dict['camera'] = (exif_data['Make'] + ' ' + exif_data['Model']).upper()
        
    image_df=image_df.append(image_dict,ignore_index=True)

image_df['date']=pd.to_datetime(image_df['date'], format='%Y:%m:%d %H:%M:%S')
image_df=image_df.sort_values(by="date")

filtered_df = image_df