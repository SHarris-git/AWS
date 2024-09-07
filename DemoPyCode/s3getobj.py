import boto3
import logging
from botocore.exceptions import ClientError

# Initialize logging
logger = logging.getLogger(__name__)

def get_object(bucket, object_key):
    # Initialize S3 resource
    s3 = boto3.resource('s3')
    
    try:
        # Access the S3 object
        obj = s3.Object(bucket, object_key)
        body = obj.get()['Body'].read()
        logger.info("Got object '%s' from bucket '%s'.", object_key, bucket)
    except ClientError:
        logger.exception("Couldn't get object '%s' from bucket '%s'.", object_key, bucket)
        raise
    else:
        return body

# Example usage
bucket_name = 'demo-content-classes'
object_key = 's3/s3_select_query.txt'  # Example: 'folder/file.txt'
content = get_object(bucket_name, object_key)

# Print or process the content of the object as needed
print(content.decode('utf-8'))  # assuming the content is text-based