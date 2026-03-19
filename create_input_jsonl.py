import json
import os
from google.cloud import storage
from dotenv import load_dotenv
from models import TestEntry

load_dotenv()

# get environment variables
BUCKET_NAME = os.environ.get("BUCKET_NAME")
INPUT_FOLDER = os.environ.get("INPUT_FOLDER")
INPUT_JSONL_NAME = os.environ.get("INPUT_JSONL_NAME")
PROMPT = os.environ.get("PROMPT")

# initialize client and get the bucket
client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)

# get all files in the specified input folder
blobs = bucket.list_blobs(prefix=INPUT_FOLDER)

# generate the input JSONL file
with open(INPUT_JSONL_NAME, "w") as f:
    for blob in blobs:
        # use the filename as the unique 'key'
        filename = blob.name.replace(INPUT_FOLDER + "/", "")
        
        # construct the request
        request = {
            "key": filename, 
            "request": {
                "contents": [{
                    "role": "user",
                    "parts": [
                        {"text": PROMPT},
                        {"file_data": {
                            "mime_type": "text/plain", 
                            "file_uri": f"gs://{BUCKET_NAME}/{blob.name}"
                        }}
                    ]
                }],
                'generation_config': {
                    'temperature': 0.0,
                    'response_mime_type': 'application/json',
                    'response_schema': TestEntry.model_json_schema()
                }
            }
        }

        # write the request as a JSON object to the JSONL file
        f.write(json.dumps(request) + "\n")
        

print(f"✅ Successfully Created {INPUT_JSONL_NAME} locally.")
