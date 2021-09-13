# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:10:36 2021

@author: Josel
"""

import threading
from webServer import run_webserver
from photoFrame import run_photoframe



#%%

try: 
    photoFrame = threading.Thread(target = run_photoframe)
    photoFrame.start()
except Exception as e:
    print('Cannot run photoframe:',e)

try:
    webServer = threading.Thread(target = run_webserver)
    webServer.start()
except Exception as e:
    print('Cannot run webServer: ',e)