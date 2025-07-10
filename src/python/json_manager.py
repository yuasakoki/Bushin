# src/python/storage_manager.py
# google-cloudとの連携を行うためのクラス
import json
from google.cloud import firestore
from google.cloud import storage

BUCKET_NAME = 'bushin-json'  # ご自身のバケット名
PLAYER_BLOB_NAME = 'names.json'
REFEREE_BLOB_NAME = 'Referee.json'

def download_json_from_gcs(blob_name=PLAYER_BLOB_NAME):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    if not blob.exists():
        return []
    return json.loads(blob.download_as_text())

def upload_json_to_gcs(data, blob_name=PLAYER_BLOB_NAME):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data, ensure_ascii=False, indent=2), content_type='application/json')

# プレイヤー用
def download_player_json_from_gcs():
    return download_json_from_gcs(PLAYER_BLOB_NAME)

def upload_player_json_to_gcs(data):
    upload_json_to_gcs(data, PLAYER_BLOB_NAME)

# 審判用
def download_referee_json_from_gcs():
    return download_json_from_gcs(REFEREE_BLOB_NAME)

def upload_referee_json_to_gcs(data):
    upload_json_to_gcs(data, REFEREE_BLOB_NAME)
