from typing import Any, Dict

import json
from pathlib import Path

from aqt import mw


ADDON_PATH = Path(mw.pm.addonFolder()) / __package__
DATA_PATH = ADDON_PATH / "user_data" / "data.json"

_data: Dict[str, Any] = {}
_tag_data: Dict[str, Any] = _data.get("tags", {})


def tag_data():
    return _tag_data


def save():
    global _data
    _data["tags"] = _tag_data
    _data_str = json.dumps(_data)

    with DATA_PATH.open(mode="w", encoding="UTF-8") as data_file:
        data_file.write(_data_str)


def read():
    global _data
    with DATA_PATH.open(encoding="UTF-8") as data_file:
        _data = json.load(data_file)


if not DATA_PATH.parent.exists():
    DATA_PATH.parent.mkdir(exist_ok=True)
elif not DATA_PATH.exists():
    save()
else:
    read()
