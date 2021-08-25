from typing import Optional, Dict
import json, os

from aqt import mw


PATH = os.path.join(mw.pm.addonFolder(), __package__)
DATA_PATH = os.path.join(PATH, "user_data", "data.json")


def tag_data():
    return _tag_data


def save():
    _data["tags"] = _tag_data
    _data_str = json.dumps(_data)
    with open(DATA_PATH, mode="w", encoding="UTF-8") as file:
        file.write(_data_str)


with open(DATA_PATH, encoding="UTF-8") as file:
    _data = json.load(file)
_tag_data = _data.get("tags", {})
