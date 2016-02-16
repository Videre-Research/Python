

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

https://github.com/VidereResearch/Python

Upload a single file to an AWS S3 bucket

'''

__author__ = "Videre Research, LLC"
__license__ = "GNU GPL V3"
__version__ = "1.0.1"
   
    
# I M P O R T S ###############################################################

from boto.s3.key import Key
from boto.s3.connection import S3Connection

import my_aws


# G L O B A L S ###############################################################


my_bucket = 'Name of your Bucket'
my_file_name = 'Name of the file you want to upload'

# C O D E #####################################################################



conn = S3Connection(my_aws.AWS_ACCESS_KEY_ID, my_aws.AWS_SECRET_ACCESS_KEY)

#Create the bucket if need be
#bucket = conn.create_bucket(my_bucket)

bucket = conn.get_bucket(my_bucket)


k = Key(bucket)
k.key = my_file_name
k.get_contents_to_filename(my_file_name)

#Optional - set the file permissions to public (for web-enabled buckets)
k.set_acl('public-read')
