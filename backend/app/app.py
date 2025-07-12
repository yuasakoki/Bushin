## backend\app\app.py
import os
import threading
from flask import Flask, request, jsonify, render_template
from datetime import datetime
from flask_cors import CORS
from .utils import validate_name
import logging

logging.basicConfig(level=logging.DEBUG)

IS_RENDER = os.environ.get("RENDER") == "1"
if IS_RENDER:
    from .firestore_manager import (
        download_player_data,
        upload_player_data,
        download_referee_data,
        upload_referee_data,
    )

    player_load_data = download_player_data
    player_save_data = upload_player_data
    referee_load_data = download_referee_data
    referee_save_data = upload_referee_data
else:
    from .local_data_manager import (
        player_load_data,
        player_save_data,
        referee_load_data,
        referee_save_data,
    )

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static",
    template_folder=os.path.join(BASE_DIR, "templates"),
)

ERROE_MWSSAGWE = "内部サーバーエラーが発生しました"

CORS(app)
file_lock = threading.Lock()


@app.route("/")
def index():
    return render_template("index.html")


# 選手名前登録API
@app.route("/api/names", methods=["POST"])
def add_name():
    logging.debug("/api/names POST request received")
    try:
        if not request.is_json:
            return (
                jsonify({"error": "リクエストボディはJSON形式である必要があります"}),
                400,
            )

        name = request.json.get("name")
        grade = request.json.get("grade")
        age = request.json.get("age")
        gender = request.json.get("gender")
        affiliation = request.json.get("affiliation")

        is_valid, result = validate_name(name)
        if not is_valid:
            return jsonify({"error": result}), 400
        name = result

        with file_lock:
            data = player_load_data()

            # 同一人物の重複チェック（複数項目で一致するか確認）
            for item in data:
                if (
                    item["name"] == name
                    and item.get("grade") == grade
                    and item.get("age") == age
                    and item.get("gender") == gender
                    and item.get("affiliation") == affiliation
                ):
                    return jsonify({"error": "この選手はすでに登録されています"}), 409

            new_entry = {
                "id": len(data) + 1,
                "name": name,
                "grade": grade,
                "age": age,
                "gender": gender,
                "affiliation": affiliation,
                "rounds": [
                    {
                        "round": 1,
                        "court_code": "",
                        "score": 0,
                    },
                    {
                        "round": 2,
                        "court_code": "",
                        "score": 0,
                    },
                    {
                        "round": 3,
                        "court_code": "",
                        "score": 0,
                    }
                ],
            }
            data.append(new_entry)

            player_save_data(data)

        return (
            jsonify({"message": "名前が正常に追加されました", "data": new_entry}),
            201,
        )

    except Exception as e:
        return jsonify({"error": ERROE_MWSSAGWE + e}), 500


# 選手名前一覧取得API
@app.route("/api/names", methods=["GET"])
def get_names():
    try:
        with file_lock:
            data = player_load_data()
        return (
            jsonify(
                {"message": "名前一覧を取得しました", "data": data, "count": len(data)}
            ),
            200,
        )
    except Exception as e:
        return jsonify({"error": ERROE_MWSSAGWE + e}), 500


# 審判員名前登録API
@app.route("/api/Referee", methods=["POST"])
def add_referee_name():
    try:
        if not request.is_json:
            return (
                jsonify({"error": "リクエストボディはJSON形式である必要があります"}),
                400,
            )

        name = request.json.get("name")

        is_valid, result = validate_name(name)
        if not is_valid:
            return jsonify({"error": result}), 400
        name = result

        with file_lock:
            data = referee_load_data()

            # 同一人物の重複チェック（名前のみ）
            for item in data:
                if item["name"] == name:
                    return jsonify({"error": "この審判員はすでに登録されています"}), 409

            new_entry = {
                "name": name,
                "created_at": datetime.now().isoformat(),
                "id": len(data) + 1,
            }
            data.append(new_entry)

            referee_save_data(data)

        return (
            jsonify({"message": "名前が正常に追加されました", "data": new_entry}),
            201,
        )

    except Exception as e:
        return jsonify({"error": ERROE_MWSSAGWE + e}), 500


# 審判員名前一覧取得API
@app.route("/api/Referee", methods=["GET"])
def get_referee_names():
    try:
        with file_lock:
            data = referee_load_data()
        return (
            jsonify(
                {"message": "名前一覧を取得しました", "data": data, "count": len(data)}
            ),
            200,
        )
    except Exception as e:
        return jsonify({"error": ERROE_MWSSAGWE + e}), 500


# エラーハンドラー
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "エンドポイントが見つかりません"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "許可されていないメソッドです"}), 405


@app.errorhandler(500)
def internal_error(error):
        return jsonify({"error": ERROE_MWSSAGWE + error}), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
