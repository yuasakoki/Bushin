# src/python/utils.py

def validate_name(name):
    if not isinstance(name, str):
        return False, "名前は文字列である必要があります"
    if len(name) > 10:
        return False, "名前は10文字以内にしてください"
    return True, name