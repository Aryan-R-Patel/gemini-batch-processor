import json
import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

# get environment variables
BUCKET_NAME = os.environ.get("BUCKET_NAME")
OUTPUT_JSONL_PATH = os.environ.get("OUTPUT_JSONL_PATH") 
OUTPUT_FOLDER = os.environ.get("OUTPUT_FOLDER")

def process_results():
    """
    Processes the output JSONL file and saves it as individual JSON files in the specified output folder in the bucket.
    """
    # initialize client and get the bucket
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)

    # get the output JSONL file in the results folder path
    blobs = bucket.list_blobs(prefix=OUTPUT_JSONL_PATH)
    output_blob = None
    for blob in blobs:
        if "predictions.jsonl" in blob.name:
            output_blob = blob
            break
            
    if not output_blob:
        print("Could not find the output file. Please check whether the job has finished and whether the OUTPUT_JSONL_PATH is correct.")
        return

    # read the output.jsonl file
    print(f"Reading results from {output_blob.name}.")
    content = output_blob.download_as_text()

    for line in content.strip().split('\n'):
        if not line:
            continue
            
        data = json.loads(line)
        original_filename = data.get("key")
        
        try:
            # extract the JSON from the response
            raw_text = data["response"]["candidates"][0]["content"]["parts"][0]["text"]
            
            # parse into a real JSON object
            structured_data = json.loads(raw_text)
            
            # save as a new JSON file in the output folder in the bucket
            json_filename = original_filename.replace(".txt", ".json")
            new_file_name = f"{OUTPUT_FOLDER}/{json_filename}"
            new_blob = bucket.blob(new_file_name)
            new_blob.upload_from_string(
                json.dumps(structured_data, indent=2),  # indent for readability
                content_type='application/json'
            )
            
            print(f"✅ Saved {new_file_name} to the bucket.")
        except Exception as e:
            print(f"⚠️ Failed to process {original_filename}: {e}")


if __name__ == "__main__":
    process_results()
