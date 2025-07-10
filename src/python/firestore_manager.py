# src/python/storage_manager.py
from google.cloud import firestore

# コレクション名
PLAYER_COLLECTION = "PLAYER"
SCORE_COLLECTION = "SCORE"
REFEREE_COLLECTION = "REFEREE"
REFEREE_ASSIGN_COLLECTION = "REFEREE_ASSIGN"

db = firestore.Client()


# 共通読み込み関数
def download_data_from_firestore(collection_name, doc_id=DEFAULT_DOC_ID):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}


# 共通書き込み関数
def upload_data_to_firestore(data, collection_name, doc_id=DEFAULT_DOC_ID):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(data)  # 上書き保存


# プレイヤー用
def download_player_data():
    return download_data_from_firestore(PLAYER_COLLECTION)


def upload_player_data(data):
    upload_data_to_firestore(data, PLAYER_COLLECTION)


# 審判用
def download_referee_data():
    return download_data_from_firestore(REFEREE_COLLECTION)


def upload_referee_data(data):
    upload_data_to_firestore(data, REFEREE_COLLECTION)
