#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/VidereResearch/Python

Recursively upload all files matching a list of extensions from a local system to an AWS S3 bucket
'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################


from boto.s3.key import Key
from boto.s3.connection import S3Connection
from glob import iglob
import logging
import sys
import os

import my_aws

# G L O B A L S ###############################################################


my_bucket = 'Name of your Bucket'
PATH = 'Path to your files'

# F U N C T I O N S ###########################################################



def main():
    conn = S3Connection(my_aws.AWS_ACCESS_KEY_ID, my_aws.AWS_SECRET_ACCESS_KEY)

    #Upload all files to a bucket and delete local copies
    logging.basicConfig(filename="s3_download.log", level=logging.INFO)
    bucket = conn.get_bucket(my_bucket)
    k = Key(bucket)
    for filename in iglob(os.path.join(PATH, 'image*.jpg')):
        print filename
        try:
            k.key = filename
            k.set_contents_from_filename(filename)
            #If the bucket is web-enabled let's make the file public readable
            k.set_acl('public-read')
            print k.name + " " + str(k.size)
            #If the size of the files are the same, the upload was successful
            #and we can delete the local file?
            statinfo = os.stat(filename)
            if k.size == statinfo.st_size:
                #uncomment the line below if you want to delete the local file
                #os.remove(filename)
            else:
                logging.info(filename + " *** NOT DELETED " + str(k.size))
        except Exception, e:
            print 'Error %s' % e
            logging.error(filename + " upload failed: " + str(e))

            
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################









