#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Plot all the location you have visited on a map by using your photos' geolocation data

Recursively scans folders of photos and gathers GPS location data (GeoTag) whenever available.
Consolidates location data within a given radius into a single record, and stores location
data into a JSON file that can be used by the enclosed HTML file to display location on a Google map.

Usage: watson_nlc_classify.py <Classifier_ID> "<question>"
#   where <Classifier_ID> is a trained and available Classifier (see watson_nlc_create.py and watson_nlc_list.py)
#   and "<question>" represents the text to be classified
'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

"""
Required Python library to natively read EXIF data from images.
https://github.com/bennoleslie/pexif
"""
from pexif import JpegFile

import sys
import glob
import math
import json
import os


# G L O B A L S ###############################################################


#The list of images extensions to consider
included_extenstions = ['jpg', 'JPG', 'jpeg', 'JPEG']

#The directory you want to scan
searchPath = '/Volumes/Data 2/Photos' 
#searchPath = '/Volumes/2TB/Stuff/Media' 

#The name of the JSON file that will be created
jsonfilename = 'photos.json'

#Consolidate location points within a certain distance (in KM) of another existing point
distanceKM = 10


# F U N C T I O N S ###########################################################


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees).
    Source: http://gis.stackexchange.com/a/56589/15183
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km


def main():

    try:
        #If a JSON file already exists, let's load the existing location data
        positionList=[]
        if os.path.isfile(jsonfilename):
            with open(jsonfilename) as f:
                jsonList = json.load(f)
            for item in jsonList:
                lat = item['lat']
                lng = item['lng']
                positionList.append((lat, lng))
        else:
            #Otherwise we'll sart with an empty list
            jsonList = []
    except:
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error:", value

    print positionList

    for dirname, dirnames, filenames in os.walk(searchPath):
        for subdirname in dirnames:
            print "FOUND DIRECTORY: ", os.path.join(dirname, subdirname)
        for filename in filenames:
            if any(filename.endswith(ext) for ext in included_extenstions):
                image = os.path.join(dirname, filename)
                print "FOUND FILE: ", image

                alreadyInList = False
                try:
                    ef = JpegFile.fromFile(image)
                    for position in positionList:
                        myDistance = haversine(position[0], position[1], lat, lng)
                        if myDistance < distanceKM:
                            alreadyInList = True
                            pass
                    if not alreadyInList:
                        print "new location"
                        jsonList.append({"lat": lat, "lng": lng, "DateTimeOriginal": ef.exif.primary.ExtendedEXIF.DateTimeOriginal, "file": image})
                        positionList.append(ef.get_geo())

                except IOError:
                    type, value, traceback = sys.exc_info()
                    print >> sys.stderr, "Error opening file:", value
                except JpegFile.NoSection:
                    type, value, traceback = sys.exc_info()
                    print >> sys.stderr, "Error get GPS info:", value
                except JpegFile.InvalidFile:
                    type, value, traceback = sys.exc_info()
                    print >> sys.stderr, "Error opening file:", value
                except:
                    type, value, traceback = sys.exc_info()
                    print >> sys.stderr, "Error:", value

    with open(jsonfilename, 'w') as outfile:
        json.dump(jsonList, outfile)
    
    
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################
