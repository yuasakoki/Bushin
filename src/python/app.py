import os
import json
import threading
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# 定数定義
DATA_DIR = 'data'
DATA_FILE = os.path.join(DATA_DIR, 'names.json')

# スレッドセーフティのためのロック
file_lock = threading.Lock()

def ensure_data_directory():
    """データディレクトリが存在することを確認"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data():
    """データファイルを読み込む"""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"データファイルの読み込みエラー: {e}")
        return []

def save_data(data):
    """データファイルに保存する"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"データファイルの保存エラー: {e}")
        return False

def validate_name(name):
    """名前のバリデーション"""
    if not name:
        return False, "名前は必須です"
    
    if not isinstance(name, str):
        return False, "名前は文字列である必要があります"
    
    name = name.strip()
    if not name:
        return False, "名前は空白のみにはできません"
    
    if len(name) > 100:
        return False, "名前は100文字以内にしてください"
    
    return True, name

# 名前登録API
@app.route('/api/names', methods=['POST'])
def add_name():
    try:
        # リクエストボディの検証
        if not request.is_json:
            return jsonify({'error': 'リクエストボディはJSON形式である必要があります'}), 400
        
        name = request.json.get('name')
        
        # 名前のバリデーション
        is_valid, result = validate_name(name)
        if not is_valid:
            return jsonify({'error': result}), 400
        
        name = result  # バリデーション後の名前を使用
        
        # スレッドセーフな処理
        with file_lock:
            # データディレクトリの作成
            ensure_data_directory()
            
            # データの読み込み
            data = load_data()
            
            # 重複チェック
            existing_names = [item['name'] for item in data]
            if name in existing_names:
                return jsonify({'error': '同じ名前が既に登録されています'}), 409
            
            # 新しいデータの追加
            new_entry = {
                'name': name,
                'created_at': datetime.now().isoformat(),
                'id': len(data) + 1
            }
            data.append(new_entry)
            
            # データの保存
            if not save_data(data):
                return jsonify({'error': 'データの保存に失敗しました'}), 500
        
        return jsonify({
            'message': '名前が正常に追加されました',
            'data': new_entry
        }), 201
        
    except Exception as e:
        print(f"予期しないエラー: {e}")
        return jsonify({'error': '内部サーバーエラーが発生しました'}), 500

# 名前一覧取得API（追加）
@app.route('/api/names', methods=['GET'])
def get_names():
    try:
        with file_lock:
            data = load_data()
        
        return jsonify({
            'message': '名前一覧を取得しました',
            'data': data,
            'count': len(data)
        }), 200
        
    except Exception as e:
        print(f"予期しないエラー: {e}")
        return jsonify({'error': '内部サーバーエラーが発生しました'}), 500

# エラーハンドラー
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'エンドポイントが見つかりません'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': '許可されていないメソッドです'}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': '内部サーバーエラーが発生しました'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)