import boto3
import os
import concurrent.futures


# This sets content type to image
import os
def copy_image(filepath):

    AWS_ACCESS_KEY_ID=''
    AWS_SECRET_ACCESS_KEY=''
    AWS_DEFAULT_REGION=''
    D_AWS_BUCKET=''
    AWS_NAMESPACE=''

    s3_d_client = boto3.client(
        's3', 
        aws_access_key_id=AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
        region_name=AWS_DEFAULT_REGION
    )

    AWS_ACCESS_KEY_ID=''
    AWS_SECRET_ACCESS_KEY=''
    AWS_DEFAULT_REGION=''
    U_AWS_BUCKET=''
    AWS_NAMESPACE=''

    s3_u_client = boto3.client(
        's3', 
        aws_access_key_id=AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
        region_name=AWS_DEFAULT_REGION
    )

    

    s3_d_client.download_file(D_AWS_BUCKET, key, filepath)


    s = s3_u_client.upload_file(filepath, U_AWS_BUCKET, key,ExtraArgs={'ACL': 'private','ContentType': 'image/jpeg',})
    os.remove(filepath)
    
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(copy_image, []) #pass 2nd parm as iterator
