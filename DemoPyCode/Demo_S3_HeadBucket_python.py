# GSH
# Run code from Cloud9. Checks if provided bucket name exists.
import boto3
from botocore.exceptions import ClientError

def check_bucket_exists(bucket_name):
    """
    Check if an S3 bucket exists using the HeadBucket API call.
    
    :param bucket_name: Name of the bucket to check
    :return: True if the bucket exists, False if it doesn't
    """
    s3_client = boto3.client('s3')
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' exists.")
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            print(f"Bucket '{bucket_name}' does not exist.")
            return False
        elif error_code == '403':
            print(f"Private bucket '{bucket_name}'. Forbidden access.")
            return True
        else:
            print(f"An error occurred: {e}")
            return False

# Example usage
bucket_name = '<enter_bucket_name_here>'
result = check_bucket_exists(bucket_name)
print(f"Bucket check result: {result}")