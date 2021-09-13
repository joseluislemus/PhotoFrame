# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:16:19 2021

@author: Josel
"""

#import dash
#import dash_core_components as dcc
#import dash_html_components as html
#from dash.dependencies import Input, Output
#
#app = dash.Dash(__name__)
#
#app.layout = html.Div


from flask import Flask
import globalVars as glb

def run_webserver():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return "Setting: Period: " + str(glb.delay_seconds) + " sec, directory: " + str(glb.photos_directory)
    
    app.run(host="0.0.0.0",debug=True, use_reloader=False)
    

