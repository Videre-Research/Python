#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

https://github.com/VidereResearch/Python

Calculates the number of files and the total size of an AWS S3 bucket

'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

from boto.s3.key import Key
from boto.s3.connection import S3Connection
import os

import my_aws

# G L O B A L S ###############################################################

my_bucket = 'Name of your S3 Bucket'

# F U N C T I O N S ###########################################################

def main():

    bucket = conn.get_bucket(my_bucket)
    for key in bucket:
        keyString = str(key.key)
        extension = os.path.splitext(keyString)[1]
        if extension in extensions:
            print key.name
            if key.name.endswith('.jpg'):
                contentType = 'image/jpeg'
            elif key.name.endswith('.png'):
                contentType = 'image/png'
            else:
                continue

            key.metadata.update({
            'Content-Type': contentType,
            'Cache-Control': 'max-age=864000'
            })
            key.copy(
                key.bucket.name,
                key.name,
                key.metadata,
                preserve_acl=True
            )

               
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################


