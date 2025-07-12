# src/python/data_manager.py
import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYER_DATA_PATH = os.path.join(BASE_DIR, "data", "names.json")
REFEREE_DATA_PATH = os.path.join(BASE_DIR, "data", "Referee.json")

def player_load_data():
    if not os.path.exists(PLAYER_DATA_PATH):
        return []
    with open(PLAYER_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)

def player_save_data(data):
    with open(PLAYER_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def referee_load_data():
    if not os.path.exists(REFEREE_DATA_PATH):
        return []
    with open(REFEREE_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)

def referee_save_data(data):
    with open(REFEREE_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)