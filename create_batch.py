import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# get environment variables
PROJECT_ID = os.environ.get("PROJECT_ID")
MODEL_ID = os.environ.get("MODEL_ID")
LOCATION = os.environ.get("LOCATION")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
BATCH_NAME = os.environ.get("BATCH_NAME")
INPUT_JSONL_NAME = os.environ.get("INPUT_JSONL_NAME")
JSONL_FOLDER = os.environ.get("JSONL_FOLDER")

# initialize client with vertex ai
client = genai.Client(
    vertexai=True, 
    project=PROJECT_ID, 
    location=LOCATION
)

# create batch job
batch_job = client.batches.create(
    model=MODEL_ID,
    src=f"gs://{BUCKET_NAME}/{JSONL_FOLDER}/{INPUT_JSONL_NAME}",
    config=types.CreateBatchJobConfig(
        display_name=BATCH_NAME,
        dest=f"gs://{BUCKET_NAME}/{JSONL_FOLDER}/"
    )
)

print("--------------------------------------------------")
print(f"Batch Job created successfully.")
print(f"Job Name: {batch_job.name}")
print(f"View progress in Console: https://console.cloud.google.com/vertex-ai/batch-predictions?project={PROJECT_ID}")
print("--------------------------------------------------")
