Using Amazon Web Services with Python
========================================

These are a few examples on how to use some of the AWS services with Python


## Requirements:

* **The Boto library** - `pip install boto`
* **AWS service credentials** 
  
    The file `my_aws.py` is a simple way to share your AWS credentials between all of the different scripts.

        my_aws.AWS_ACCESS_KEY_ID = "Your AWS Access Key ID"
        my_aws.AWS_SECRET_ACCESS_KEY = "Your AWS Secret Access Key"


## Working with AWS S3 buckets

AWS S3 storage is a powerful and inexpensive solution for storing files on the cloud. The management web interface is still a little clunky, but a rich set of APIs exposed through the boto library can help.
    
    S3_Download.py      Download a single file from AWS S3 to your system
    S3_Download_all.py  Recursively download files from AWS S3 to your system
    S3_Upload.py        Upload a single file from your system to AWS S3
    S3_Upload_all.py    Recursively upload files from your system to AWS S3
    S3_Total_Size.py    Prints the total size and number of files in an S3 bucket
    S3_Update_Cache.py  Updates the cache information of images in a web-enabled S3 bucket

## Route 53 DNS

