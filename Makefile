# BATCH CREATION PIPELINE
batch: create_input_jsonl upload_input_jsonl create_batch

create_input_jsonl:
	python create_input_jsonl.py

upload_input_jsonl: create_input_jsonl
	python upload_input_jsonl.py

create_batch: upload_input_jsonl
	python create_batch.py

# POST-PROCESSING PIPELINE
post_process:
	python post_process.py
