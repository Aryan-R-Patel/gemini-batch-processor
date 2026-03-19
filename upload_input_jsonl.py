import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

# get environment variables
BUCKET_NAME = os.environ.get("BUCKET_NAME")
INPUT_JSONL_NAME = os.environ.get("INPUT_JSONL_NAME")
JSONL_FOLDER = os.environ.get("JSONL_FOLDER")

# initialize client and get the bucket
client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)

# upload input JSONL file to the specified folder in bucket
destination_blob_path = f"{JSONL_FOLDER}/{INPUT_JSONL_NAME}"
blob = bucket.blob(destination_blob_path)
blob.upload_from_filename(INPUT_JSONL_NAME)


print(f"✅ Successfully uploaded {INPUT_JSONL_NAME} to {destination_blob_path} in bucket {bucket.name}.")
