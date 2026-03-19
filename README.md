# Gemini Batch Processor
A Python application that processes documents in batches using **Google Gemini, Cloud Storage Buckets,** and **Batch API.**

## Installation and Setup
### Google Cloud Project and Storage Bucket
1. Create a Google Cloud Project.
2. Create a Google Cloud Storage Bucket.
    - Select a **Location Type** (e.g. "Region") and a **Location** (e.g. "northamerica-northeast2 (Toronto)")
    - Select **Default** Storage Class
    - Use the default settings for the rest of the prompts.
3. Create 3 folders inside your bucket. 
    - Input Folder (this is where you will upload all the original data)
    - JSONL Folder (this is where the script will upload and generate JSONL files)
    - Output Folder (this is where the resulting data will be stored)

### Google Cloud CLI
1. Install [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
2. Initialize and authorize the gcloud CLI by running `gcloud init`. This will open a web browser to authorize access. Follow the instructions to complete the process. For more information and troubleshooting, refer to the documentation [here](https://docs.cloud.google.com/sdk/docs/install-sdk#:~:text=changes%20take%20effect.-,Initialize%20and%20authorize%20the%20gcloud%20CLI,-If%20you%20are).
3. Run `gcloud auth application-default login` to establish a connection between the code and the Google Cloud API. You will be redirected to the browser. Follow the instructions to complete the process. You will see a notice `"You are now authenticated with the gcloud CLI!"` if your setup was completed successfully.

### Virtual Environment
1. Create a Python virtual environment: `python3 -m venv venv`.
2. Activate the virtual environment: `source venv/bin/activate`.
3. Install dependencies and packages: `pip install -r requirements.txt`.
4. Fill the `.env.template` with your credentials and save it as `.env`. Follow the instructions in [docs](./docs/).

## Demo Usage
There is some sample data provided in the `sample_data` [directory](./sample_data/).
It contains 10 text documents, each containing 1 paragraph of text. Our goal is to process these documents in a batch and generate output documents that contain the 'topic' and 'summary' for each of the input documents in JSON format.

1. Upload the sample data to the Input Folder of your bucket.
2. Run `make batch`. This will create an input JSONL file, upload it to the JSONL Folder, and then create a batch job using that JSONL file. 
3. After the batch job is finished, we need to update the .env file. Enter the folder name of your output JSONL file from your bucket in `OUTPUT_JSONL_PATH`.
4. Run `make post_process`. This will process our documents using the output JSONL file and our Output Folder in the bucket will be populated with our desired data.


## Additional Documentation
See more detailed documentation [here](./docs/).
