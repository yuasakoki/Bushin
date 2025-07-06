# src/python/storage_manager.py
import json
from google.cloud import storage

BUCKET_NAME = 'bushin-json'  # 自分のバケット名に変えてください
BLOB_NAME = 'names.json'

def download_json_from_gcs():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(BLOB_NAME)
    if not blob.exists():
        return []
    return json.loads(blob.download_as_text())

def upload_json_to_gcs(data):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(BLOB_NAME)
    blob.upload_from_string(json.dumps(data, ensure_ascii=False, indent=2), content_type='application/json')
