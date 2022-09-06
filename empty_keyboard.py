import json
def get_empty_keyboard():
    empty_keyboard = {
        "one_time": False,
        "buttons": []
    }
    empty_keyboard = json.dumps(empty_keyboard, ensure_ascii=False).encode('utf-8')
    return empty_keyboard