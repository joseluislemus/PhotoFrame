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


from flask import Flask,request,render_template
from datetime import datetime
import globalVars as glb

def run_webserver():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        try:
            parameterDict = eval(request.args.get('p'))
        except:
            parameterDict = None
        
        if type(parameterDict)==dict:
            
            #period
            if 'period' in parameterDict:
                try:
                    new_delay_seconds = int(parameterDict['period'])
                    if new_delay_seconds < glb.delay_seconds_min:
                        glb.delay_seconds = glb.delay_seconds_min
                    elif new_delay_seconds > glb.delay_seconds_max:
                        glb.delay_seconds = glb.delay_seconds_max
                    else:
                        glb.delay_seconds = new_delay_seconds
                except:
                    pass
            
            #random
            if 'random' in parameterDict:
                if parameterDict['random'] == 1: glb.randomize = True
                elif parameterDict['random'] == 0: glb.randomize = False

            #startDate
            if 'sdate' in parameterDict:
                try:
                    glb.start_date = datetime.strptime(parameterDict['sdate'], '%Y:%m:%d:%H:%M')
                except:
                    pass
            
            #endDate
            if 'edate' in parameterDict:
                try:
                    glb.end_date = datetime.strptime(parameterDict['edate'], '%Y:%m:%d:%H:%M')
                except:
                    pass
        current_photo_dict = glb.image_df[glb.image_df.filename == glb.current_image].to_dict(orient='records')[0]
        return render_template('index.html', 
                               title='Photoframe',
                               content="Setting: Period: " + str(glb.delay_seconds) + " sec, directory: " + str(glb.photos_directory),
                               current_photo_info = current_photo_dict )
    
#    @app.route("/params/")
#    def get_params():
#        try:
#            parameterDict = eval(request.args.get('p'))
#        except:
#            parameterDict = None
#        
#        if type(parameterDict)==dict:
#            
#            #period
#            if 'period' in parameterDict:
#                try:
#                    new_delay_seconds = int(parameterDict['period'])
#                    if new_delay_seconds < glb.delay_seconds_min:
#                        glb.delay_seconds = glb.delay_seconds_min
#                    elif new_delay_seconds > glb.delay_seconds_max:
#                        glb.delay_seconds = glb.delay_seconds_max
#                    else:
#                        glb.delay_seconds = new_delay_seconds
#                except:
#                    pass
#            
#            #random
#            if 'random' in parameterDict:
#                if parameterDict['random'] == 1: glb.randomize = True
#                elif parameterDict['random'] == 0: glb.randomize = False
#
#            #startDate
#            if 'sdate' in parameterDict:
#                try:
#                    glb.start_date = datetime.strptime(parameterDict['sdate'], '%Y:%m:%d:%H:%M')
#                except:
#                    pass
#            
#            #endDate
#            if 'edate' in parameterDict:
#                try:
#                    glb.end_date = datetime.strptime(parameterDict['edate'], '%Y:%m:%d:%H:%M')
#                except:
#                    pass
#            

   
    app.run(host="0.0.0.0",debug=True, use_reloader=False)
    
    
    #    def get_ordered_sequences():
#    try:
#        partialSequence = ast.literal_eval(request.args.get('partialSequence'))
#    except:
#        partialSequence = None
#    if partialSequence and type(partialSequence)==list:
#        # looking for invalid elements
#        for v in partialSequence:
#            if not(v.startswith("(SEARCH) ")) and not(v.startswith("(FILTER) ")):
#                if v not in all_options:
#                    sequences = []
#                    status = "Unnexpected element provided: '{}'. All valid elements can be accessed at /getInputOptions".format(v)
#                    result = {'sequences':sequences, 'status':status}
#                    return jsonify(result)
#        # if everything is fine
#        sequences = get_sequences(partialSequence)
#        status = 'OK'
#    else:
#        sequences = []
#        status = partialSequence
##        status = 'Empty or invalid partialSequence.'
#    result = {'sequences':sequences, 'status':status}
#    return jsonify(result)
