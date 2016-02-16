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

import my_aws

# G L O B A L S ###############################################################

my_bucket = 'Name of your S3 Bucket'

# F U N C T I O N S ###########################################################

def main():

    conn = S3Connection(my_aws.AWS_ACCESS_KEY_ID, my_aws.AWS_SECRET_ACCESS_KEY)

    bucket = conn.get_bucket(my_bucket)
    k = Key(bucket)

    size = 0
    count = 0

    for key in bucket.list():
        #This example will only count files in the "snc" folder, adjust to your needs
        if key.name[:4] == 'snc/':
            size += key.size
            count += 1
            #print key.name

    print "%.3f objects" % (count)
    print "%.3f GB" % (size*1.0/1024/1024/1024)


               
###############################################################################

if __name__ == "__main__":
    main()

# E N D   O F   F I L E #######################################################


