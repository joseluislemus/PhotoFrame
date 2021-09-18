# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:18:28 2021

@author: Josel
"""
import globalVars as glb
from PIL import Image, ImageTk 
import tkinter as tk
import random
import time
import os

class SlideShow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.maxwidth = int (self.winfo_screenheight() * 1.5)
        self.display_width = 1
        self.display_height = 1
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.lastphototime = time.time()-1000
        self.delay_seconds = glb.delay_seconds
        self.timenow = time.time()
        self.track_img_index = 0
        self.background = 'black'
        self.start_date = glb.start_date
        self.end_date = glb.end_date
        self.pictures = glb.filtered_df['filename'].tolist()
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")
        self.exif_data = {}

    def show_slides(self):
        
        if self.track_img_index < len(self.pictures) :
            self.lastphototime = time.time()
            x = self.pictures[self.track_img_index]
            glb.next_image = x
            if self.track_img_index == len(self.pictures) - 1:
                self.track_img_index = 0
            else:
                self.track_img_index +=1
            original_image = Image.open(x)
            original_width, original_height = original_image.size
            original_ratio = original_width / original_height
            
#   portraits
            if original_ratio < 1.4 :
                self.display_width = int(self.h * original_ratio)
                self.display_height = self.h
                self.background = 'white'
#   landscape
            else:
                self.display_width = self.maxwidth
                self.display_height = int(self.maxwidth / original_ratio)
                self.background = 'black'

            resized = original_image.resize(( self.display_width, self.display_height ),Image.ANTIALIAS)
            new_img = ImageTk.PhotoImage(resized)
            self.picture_display.config(image=new_img, bg = self.background)           
            self.picture_display.image = new_img
            self.title(os.path.basename(x))
            self.after(0, self.check_params)
            
            
    def check_params(self):
        while self.timenow - self.lastphototime < glb.delay_seconds:
            self.timenow = time.time()
            
            if self.delay_seconds != glb.delay_seconds:
                self.delay_seconds = glb.delay_seconds
                break
            
            if self.start_date != glb.start_date or self.end_date != glb.end_date:
                self.start_date = glb.start_date
                self.end_date = glb.end_date
                glb.filtered_df=glb.image_df[(glb.image_df['date'] > glb.start_date) & (glb.image_df['date'] < glb.end_date)]
                glb.image_files = glb.filtered_df['filename'].tolist()
                if glb.randomize: random.shuffle(glb.image_files)
                self.pictures = glb.image_files
                self.track_img_index = 0
                break

            time.sleep(1)
        
        self.after(20, self.show_slides)
        glb.current_image = glb.next_image
        
        
def run_photoframe():

    photoframe_instance = SlideShow()
    photoframe_instance.show_slides()
    photoframe_instance.mainloop()
