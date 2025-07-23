# backend\app\utils.py
import json
import os
import logging 

# ロガーの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # ターミナルへの出力
    ]
)
logger = logging.getLogger(__name__)

def validate_name(name):
    if not isinstance(name, str):
        return False, "名前は文字列である必要があります"
    if len(name) > 10:
        return False, "名前は10文字以内にしてください"
    return True, name

def load_bushin_code_master():
    json_path = os.path.join(os.path.dirname(__file__), 'data/bushin_code_master.json')

    if not os.path.exists(json_path):
        logging.error(f"[ERROR] マスターファイルが存在しません: {json_path}")
        return {}

    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_court_code(court_name: str) -> str:
    try:
        master_data = load_bushin_code_master().get("A0001", {})
        logging.debug(f"[DEBUG] A0001のマスターデータ取得: {master_data}")

        # マスターデータから逆引きマップを作成
        code_map = {}
        for code, name in master_data.items():
            code_map[name] = code

        logging.debug(f"[DEBUG] 逆引きマップ: {code_map}")

        result = code_map.get(court_name, "")
        if result:
            logging.info(f"[INFO] コート名「{court_name}」をコード「{result}」に変換成功")
        else:
            logging.warning(f"[WARN] コート名「{court_name}」の変換に失敗（マスタに存在しません）")

        return code_map.get(court_name, "")

    except Exception as e:
        logging.error(f"コート変換エラー: {e}")
        return ""

def convert_court_name(code: str) -> str:
    try:
        master_data = load_bushin_code_master().get("A0001", {})        
        # 各カテゴリーを検索 
        if code in master_data:
            return master_data[code]
        return ""

    except Exception as e:
        print(f"コート名変換エラー: {e}")
        return ""
