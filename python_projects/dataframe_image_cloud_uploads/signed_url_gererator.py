from google.cloud import storage
import datetime

def generate_signed_url(bucket_name, blob_name):
    """Generates a signed URL for a blob, which provides temporary access."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # This URL will be valid for 7 days.
    url = blob.generate_signed_url(
        expiration=datetime.timedelta(days=7),
        # Specify the HTTP method and any headers and query parameters that
        # should be included in the signed URL.
        method="GET",
    )

    print("Generated signed URL for blob: {}".format(url))
    return url

# Replace 'my_bucket' and 'my_blob' with your bucket and blob names respectively.
generate_signed_url('my_bucket', 'my_blob')
