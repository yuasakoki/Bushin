# backend\app\firestore_manager.py
import os
from google.cloud import firestore
from google.auth.credentials import AnonymousCredentials
from dotenv import load_dotenv
import logging 
from typing import List, Dict, Any, Optional
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

load_dotenv()
# ロガーの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # ターミナルへの出力
    ]
)
logger = logging.getLogger(__name__)

# コレクション名
PLAYER_COLLECTION = 'PLAYER'
REFEREE_COLLECTION = 'REFEREE'
REFEREE_ASSIGN_COLLECTION = 'REFEREE_ASSIGN'

# Firestore Clientの初期化（環境によって切り替え）
def initialize_firestore_client():
    use_emulator = os.getenv("USE_FIRESTORE_EMULATOR", "false").lower() == "true"
    if use_emulator:
        os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
        return firestore.Client(
            project="bushin-json",
            credentials=AnonymousCredentials()
        )
    else:
        # 本番用: 認証は GOOGLE_APPLICATION_CREDENTIALS を参照
        return firestore.Client()

db = initialize_firestore_client()

# 共通読み込み関数
def download_data_from_firestore(collection_name: str) -> List[Dict[str, Any]]:
    logger.info(f"Fetching data from collection: {collection_name}")
    try:
        docs = db.collection(collection_name).order_by("create_datetime", direction=firestore.Query.DESCENDING).stream()
        result = []
        
        for doc in docs:
            # Firestoreのドキュメントをdict形式に変換
            data = doc.to_dict()
            # ドキュメントIDも保存
            # data['id'] = doc.id
            
            # データ型をJSON互換に変換
            formatted_data = {
                "id": str(data.get("id", "")),
                "name": str(data.get("name", "")),
                "grade": str(data.get("grade", "")),
                "age": str(data.get("age", "")),
                "gender": str(data.get("gender", "")),
                "affiliation": str(data.get("affiliation", "")),
                "create_datetime": data.get("create_datetime", ""),
                "rounds": data.get("rounds", [
                    {"round": 1, "court_code": "", "score": 0},
                    {"round": 2, "court_code": "", "score": 0},
                    {"round": 3, "court_code": "", "score": 0}
                ])
            }
            
            result.append(formatted_data)
            
        logger.debug(f"Retrieved {len(result)} documents")
        return result

    except Exception as e:
        logger.error(f"Error fetching data from {collection_name}: {str(e)}")
        return []

# 共通書き込み関数
def upload_data_to_firestore(data, collection_name):
    # breakpoint()
    doc_ref = db.collection(collection_name).document(data.get("id",))
    doc_ref.set(data)  # 上書き保存

# 選手一覧取得
def download_player_data():
    return download_data_from_firestore(PLAYER_COLLECTION)

def upload_player_data(data):
    upload_data_to_firestore(data, PLAYER_COLLECTION)

# 審判員一覧取得
def download_referee_data():
    return download_data_from_firestore(REFEREE_COLLECTION)

def upload_referee_data(data):
    upload_data_to_firestore(data, REFEREE_COLLECTION)

# 審判員割り当て一覧取得
def download_referee_data():
    return download_data_from_firestore(REFEREE_ASSIGN_COLLECTION)

def upload_referee_data(data):
    upload_data_to_firestore(data, REFEREE_ASSIGN_COLLECTION)