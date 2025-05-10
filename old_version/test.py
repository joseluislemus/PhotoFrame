from PIL import Image, ImageTk
import tkinter as tk
import random
import glob
import time
import os

class App(tk.Tk):
    def __init__(self, image_files, delay):
        tk.Tk.__init__(self)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.maxwidth = int (self.winfo_screenheight() * 1.5)
        self.display_width = 1
        self.display_height = 1
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.delay = delay
        self.lastphototime = time.time()-1000
        self.timenow = time.time()
        self.track_img_index = 0
        self.background = 'black'
        self.pictures = image_files           
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")

    def show_slides(self):

        if self.track_img_index < len(self.pictures) :
            self.lastphototime = time.time()
            x = self.pictures[self.track_img_index]
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
        while self.timenow - self.lastphototime < self.delay:
            print(self.timenow - self.lastphototime)
            self.timenow = time.time()
#        print (time.time() - self.lastphototime)
        self.after(50, self.show_slides)

delay_seconds = 4
photos_directory = "./PhotoFrame/2021"
randomize = True

image_files = glob.glob(photos_directory + '/**/*.jpg', recursive = True)

if randomize: random.shuffle(image_files)

app = App(image_files, delay_seconds)
app.show_slides()
app.mainloop()