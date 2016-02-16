#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Saves the Text to Speech (TTS) voice as an .mp3 file
'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

import pyvona

# F U N C T I O N S ###########################################################


def main():

    
def speak(text, fileName):
    text = text.strip()
    if len(text) == 0:
        return
    voice = pyvona.create_voice('Access Key', 'Secret Key')
    #If you want to see the voices available, uncomment the line below
    #print(voice.list_voices())
    voice.voice_name = "Salli"
    voice.codec = 'mp3'
    #Save the TTS audio of 'text' as fileName.mp3 in the local folder
    voice.fetch_voice(text,fileName)


               
###############################################################################

#Change this example to use your own Text and the name of the .mp3 file you want to create
speak("Hello","hello")

# E N D   O F   F I L E #######################################################


