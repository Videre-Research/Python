#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Provides Text to Speech (TTS) function to other Python scripts
'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

import pyvona

# F U N C T I O N S ###########################################################

def speak(text):
        text = text.strip()
        if len(text) == 0:
                return
	voice = pyvona.create_voice('Access Key', 'Secret Key')
	voice.voice_name = "Salli"
	voice.speak(text)
	#print text



               
###############################################################################

#speak('Sample text')

# E N D   O F   F I L E #######################################################



