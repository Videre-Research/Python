

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

https://github.com/VidereResearch/Python

Download a single file from an AWS S3 bucket

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
my_file_name = 'Name of the file you want to download'

# C O D E #####################################################################



conn = S3Connection(my_aws.AWS_ACCESS_KEY_ID, my_aws.AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket(my_bucket)


k = Key(bucket)
k.key = my_file_name
k.set_contents_from_filename(my_file_name)
