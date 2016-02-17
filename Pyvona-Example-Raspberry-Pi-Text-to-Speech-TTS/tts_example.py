#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Randomly speaks a sentence using TTS depending on arguments passed to the script


Usage:  tts_example.py home
        tts_example.py leaving

'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

import tts
import random
import sys

# F U N C T I O N S ###########################################################


def main():

    #Prints the  arguments passed
    for arg in sys.argv:
        print arg

    home = ['Welcome home!', 
        'Hi again!', 
        'Hello there, welcome back!']

    if sys.argv[1] == "home":
        print "home"
        tts.speak(random.choice(home))

    leaving = ['See you later.',
        'Goodbye!',
        'Be safe out there!']

    if sys.argv[1] == "leaving":
        print "leaving"
        tts.speak(random.choice(leaving))


               
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################


