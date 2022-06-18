#%% -*- coding: utf-8 -*-

import glob 
from datetime import datetime
import pandas as pd
from PIL import Image,ExifTags
from fractions import Fraction

#global vars
delay_seconds = 300
delay_seconds_min = 5
delay_seconds_max = 1800

photos_directory = "./photos"
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
for index,image_file in enumerate(image_files):
    image_df.loc[index,'filename'] = image_file
    image = Image.open(image_file)
    try:
        exif_data = {ExifTags.TAGS[k]: v
                    for k, v in image._getexif().items()
                    if k in ExifTags.TAGS}
        image_df.loc[index,'date'] = exif_data['DateTimeDigitized']
        image_df.loc[index,'speed'] = str(Fraction(exif_data['ExposureTime'])) + 's'
        image_df.loc[index,'aperture'] = 'F'+str(exif_data['FNumber'])
        image_df.loc[index,'focallength'] = str(int(exif_data['FocalLength']))+'mm'
        image_df.loc[index,'iso'] = str(exif_data['ISOSpeedRatings'])
        
        if exif_data['Make'] in exif_data['Model']:
            image_df.loc[index,'camera'] = (exif_data['Model']).upper()
        else:
            image_df.loc[index,'camera'] = (exif_data['Make'] + ' ' + exif_data['Model']).upper()
    except: pass    

image_df['date']=pd.to_datetime(image_df['date'], format='%Y:%m:%d %H:%M:%S')
image_df=image_df.sort_values(by="date")

filtered_df = image_df