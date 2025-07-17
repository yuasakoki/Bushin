import os
import threading
import logging
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from .utils import validate_name
import uuid

from dotenv import load_dotenv

load_dotenv()
from .firestore_manager import (
    download_player_data as player_load_data,
    upload_player_data as player_save_data,
    download_referee_data as referee_load_data,
    upload_referee_data as referee_save_data,
)

# ロガーの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # ターミナルへの出力
    ]
)
logger = logging.getLogger(__name__)

# 定数
ERROR_MESSAGE = "内部サーバーエラーが発生しました"

# Flaskアプリ設定
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static",
    template_folder=os.path.join(BASE_DIR, "templates"),
)
CORS(app)
file_lock = threading.Lock()


# 共通エラーレスポンス
def handle_exception(e):
    logging.exception(e)
    return jsonify({"error": ERROR_MESSAGE + ": " + str(e)}), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/names", methods=["POST"])
def add_player():
    logging.debug("/api/names POST request received")
    try:
        if not request.is_json:
            return (
                jsonify({"error": "リクエストボディはJSON形式である必要があります"}),
                400,
            )

        data = request.json
        name, grade, age, gender, affiliation = (
            data.get("name"),
            data.get("grade"),
            data.get("age"),
            data.get("gender"),
            data.get("affiliation"),
        )

        is_valid, validated_name = validate_name(name)
        if not is_valid:
            return jsonify({"error": validated_name}), 400

        name = validated_name

        existing_players = player_load_data()
        logger.info(f"existing_players: {existing_players}")
        if len(existing_players) != 1:
        # 重複チェック
            for player in existing_players:
                if (
                    player.get("name") == name
                    and player.get("grade") == grade
                    and player.get("age") == age
                    and player.get("gender") == gender
                    and player.get("affiliation") == affiliation
                ):
                    return jsonify({"error": "この選手はすでに登録されています"}), 409

        new_entry = {
            "id": str(uuid.uuid4()),
            "name": name,
            "grade": grade,
            "age": age,
            "gender": gender,
            "affiliation": affiliation,
            "create_datetime": datetime.now().isoformat(),
            "rounds": [{"round": i, "court_code": "", "score": 0} for i in range(1, 4)],
        }

        player_save_data(new_entry)
        all_players = player_load_data()
        return (
            jsonify({
                "message": "名前が正常に追加されました",
                "data": all_players  # 一覧として返す
            }),
    201,
)


    except Exception as e:
        return handle_exception(e)


@app.route("/api/names", methods=["GET"])
def get_players():
    try:
        players = player_load_data()
        return (
            jsonify(
                {
                    "message": "名前一覧を取得しました",
                    "data": players,
                    "count": len(players),
                }
            ),
            200,
        )
    except Exception as e:
        return handle_exception(e)


@app.route("/api/referees", methods=["POST"])
def add_referee():
    try:
        if not request.is_json:
            return (
                jsonify({"error": "リクエストボディはJSON形式である必要があります"}),
                400,
            )

        name = request.json.get("name")
        is_valid, validated_name = validate_name(name)
        if not is_valid:
            return jsonify({"error": validated_name}), 400

        with file_lock:
            data = referee_load_data()
            if any(r["name"] == validated_name for r in data):
                return jsonify({"error": "この審判員はすでに登録されています"}), 409

            new_entry = {
                "id": len(data) + 1,
                "name": validated_name,
                "created_at": datetime.now().isoformat(),
            }
            data.append(new_entry)
            referee_save_data(data)

        return (
            jsonify({"message": "名前が正常に追加されました", "data": new_entry}),
            201,
        )

    except Exception as e:
        return handle_exception(e)


@app.route("/api/referees", methods=["GET"])
def get_referees():
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
        return handle_exception(e)


# 共通エラーハンドラ
@app.errorhandler(404)
def not_found(_):
    return jsonify({"error": "エンドポイントが見つかりません"}), 404


@app.errorhandler(405)
def method_not_allowed(_):
    return jsonify({"error": "許可されていないメソッドです"}), 405


@app.errorhandler(500)
def internal_server_error(e):
    return handle_exception(e)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
