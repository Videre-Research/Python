#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Recursively download all files from an AWS S3 bucket to the local file system
'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################


from boto.s3.key import Key
from boto.s3.connection import S3Connection
import logging
import sys
import os

import my_aws

# G L O B A L S ###############################################################


my_bucket = 'Name of your S3 Bucket'
my_folder = 'Name of the folder in the S3 bucket'
LOCAL_PATH = 'Path to your files'

# F U N C T I O N S ###########################################################


def main():
    
    conn = S3Connection(my_aws.AWS_ACCESS_KEY_ID, my_aws.AWS_SECRET_ACCESS_KEY)

    logging.basicConfig(filename="s3_download.log", level=logging.INFO)

    bucket = conn.get_bucket(my_bucket)
    rs2 = bucket.list(my_folder)
    for key in rs2:
        print key.name + " " + str(key.size)
        keyString = str(key.key)
        try:
            res = key.get_contents_to_filename(key.name)
            statinfo = os.stat(key.name)
            if key.size == statinfo.st_size:
                key.delete()
            else:
                logging.info(key.name + " *** NOT DELETED " + str(key.size))
            #break
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]

        # check if file exists locally, if not: download it
        #if not os.path.exists(LOCAL_PATH+keyString):
        #key.get_contents_to_filename(LOCAL_PATH[:-1]+keyString)

        # file_md5 = md5(res.name)
        # if file_md5 == key.hash:
        #     rs2.delete_key(key)
        #     print "OK"
        # else:
        #     print "Delete Failed"

               
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################


