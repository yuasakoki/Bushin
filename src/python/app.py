import os
import threading
from flask import Flask, request, jsonify, render_template
from datetime import datetime
from flask_cors import CORS
from .utils import validate_name
from .storage_manager import download_json_from_gcs, upload_json_to_gcs


#修正した際は以下のコマンドを実行する
#npm run build
# PS C:\work\Bushin> cp -r -Force  dist/assets/ src/python/static/   
# PS C:\work\Bushin> cp -Force  dist/index.html src/python/templates/
# PS C:\work\Bushin> cp -Force src/python/static/index.html src/python/templates/index.html
# PS C:\work\Bushin> python src/python/app.py      

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path='/static',
    template_folder=os.path.join(BASE_DIR, "templates")
)

CORS(app)
file_lock = threading.Lock()

def load_data():
    try:
        return download_json_from_gcs()
    except Exception as e:
        print(f"Error loading data from GCS: {e}")
        return []

def save_data(data):
    try:
        upload_json_to_gcs(data)
        return True
    except Exception as e:
        print(f"Error saving data to GCS: {e}")
        return False

@app.route('/')
def index():
    return render_template("index.html")

# 名前登録API
@app.route('/api/names', methods=['POST'])
def add_name():
    try:
        # todo:生年月日を取得して年齢を計算する
        if not request.is_json:
            return jsonify({'error': 'リクエストボディはJSON形式である必要があります'}), 400
        
        name = request.json.get('name')
        grade = request.json.get('grade')
        age = request.json.get('age')
        sex = request.json.get('sex')
        affiliation = request.json.get('affiliation')
        
        is_valid, result = validate_name(name)
        if not is_valid:
            return jsonify({'error': result}), 400
        name = result
        
        with file_lock:
            data = load_data()
            
             # 同一人物の重複チェック（複数項目で一致するか確認）
            for item in data:
                if (
                    item['name'] == name and
                    item.get('grade') == grade and
                    item.get('age') == age and
                    item.get('sex') == sex and
                    item.get('affiliation') == affiliation
                ):
                    return jsonify({'error': 'この選手はすでに登録されています'}), 409
            
            new_entry = {
                'name': name,
                'grade': grade,
                'age': age,
                'sex': sex,
                'affiliation': affiliation,
                'created_at': datetime.now().isoformat(),
                'id': len(data) + 1
            }
            data.append(new_entry)
            
            if not save_data(data):
                return jsonify({'error': 'データの保存に失敗しました'}), 500

        return jsonify({'message': '名前が正常に追加されました', 'data': new_entry}), 201

    except Exception as e:
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
