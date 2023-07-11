"""
Upload a dataframe full of image urls to google storage and 
sort them into folders with a given config of sorting details
and access keys
"""
from google.cloud import storage
import requests
from io import BytesIO
import pandas as pd
from config import tiles_pipeline

pipeline = tiles_pipeline()

print(pipeline.bucket_name)
df = pipeline.data
bucket_name = pipeline.bucket_name

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to the bucket.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    response = requests.get(source_file_name)
    img_data = BytesIO(response.content)
    blob.upload_from_file(img_data)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

for index, row in df.iterrows():
    collection_name = row['Collection Name'].replace(' ', '_') # Replace spaces with underscores
    product_name = row['Product Name']
    color_name = row['Color Name']
    image_url = row['Image URL']
    
    # Set the destination name of the blob
    destination_blob_name = f"{collection_name}/{product_name}/{product_name}_{color_name}.jpg"
    
    # Download and upload the image to GCS
    upload_blob(bucket_name, image_url, destination_blob_name)