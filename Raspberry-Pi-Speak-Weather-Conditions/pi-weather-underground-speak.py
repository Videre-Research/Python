#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Make a call to the Weather Underground API to retrieve the JSON-formatted weather information
and creates a human-understandable summary of the conditions.

'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################


import requests
import json
import sys

from datetime import datetime, timedelta, date

#https://github.com/VidereResearch/Python/tree/master/Pyvona-Example-Raspberry-Pi-Text-to-Speech-TTS
#Uncomment all of the 'tts.speak(text)' and the import statement below to enable Text to Speech
#import tts


# G L O B A L S ###############################################################

my_wu_api_key = 'Your API Key'
my_location = 'HI/Kihei'


# F U N C T I O N S ###########################################################


def main():

    url = 'http://api.wunderground.com/api/' + my_wu_api_key + '/geolookup/conditions/forecast/q/' + my_location + '.json'
    
    try:
        r = requests.get(url)
        print r.status_code
        if r.status_code == 200:
            data = json.loads(r.text)
        else:
            print "There was an error"
            print r.text
    except Exception, e:
        print e
        return
    
    now = datetime.now().replace(second=0, microsecond=0)
    #tts.speak(now.strftime('Today is %A %b %d and it is %I:%M %p.'))
    print now.strftime('Today is %A %b %d and it is %I:%M %p.')

    text = "The weather is currently %s." % data['current_observation']['weather']
    #tts.speak(text)
    print text

    text = "Temperature is now %s degrees. " % data['current_observation']['temp_f']
    if float(data['current_observation']['temp_f']) < 32:
            text += " It is cold! "
    if float(data['current_observation']['temp_f']) < 22:
            text += " It is really really cold! "

    if abs(float(data['current_observation']['temp_f'])-float(data['current_observation']['feelslike_f'])) > 5:
        text += " Temperature feels like %s. "% data['current_observation']['feelslike_f']
    text += " High today %s,"% data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
    text += " low %s."% data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
    #tts.speak(text)
    print text

    text=''
    if float(data['current_observation']['precip_1hr_in']) > 0.5:
            text += " It is raining."

    if float(data['current_observation']['visibility_mi']) < 5:
            text += " Low visibility %s miles. "% data['current_observation']['visibility_mi']

    if int(data['current_observation']['relative_humidity'][:-1]) > 90:
            text += " Humidity %s . " % data['current_observation']['relative_humidity']


    if int(data['forecast']['simpleforecast']['forecastday'][0]['snow_allday']['in']) > 0:
            text += " %s inches of snow expected. " % data['forecast']['simpleforecast']['forecastday'][0]['snow_allday']['in']


    if int(data['forecast']['simpleforecast']['forecastday'][0]['maxwind']['mph']) > 10:
            text += " High wind %s miles per hour. " % data['forecast']['simpleforecast']['forecastday'][0]['maxwind']['mph']

    text += " Forecast for today: "
    text += data['forecast']['txt_forecast']['forecastday'][0]['fcttext'] 

    #tts.speak(text)
    print text


              
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################

