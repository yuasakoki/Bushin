# app.py
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Flaskを起動するフォルダ内に「data」フォルダを作成し、その中に保存するのが管理しやすいです。
DATA_FILE = 'data/names.json'
# 名前一覧取得API
@app.route('/api/names', methods=['GET'])
def get_names():
    if not os.path.exists(DATA_FILE):
        return jsonify([])  # ファイルがなければ空リスト返す
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# 名前登録API
@app.route('/api/names', methods=['POST'])
def add_name():
    name = request.json.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    if not os.path.exists('data'):
        os.makedirs('data')

    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

    data.append({'name': name})

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return jsonify({'message': 'Name added', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
