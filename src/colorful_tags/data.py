# -*- coding: utf-8 -*-

# Colorful Tags for Anki
#
# Copyright (C) 2018-2021  Aristotelis P. <https//glutanimate.com/>
# Copyright (C) 2021  RumovZ <gp5glkw78@relay.firefox.com>
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from pathlib import Path
from typing import Any, Dict

from aqt import mw

ADDON_PATH = Path(mw.pm.addonFolder()) / __package__
DATA_PATH = ADDON_PATH / "user_data" / "data.json"

_data: Dict[str, Any] = {}
_tag_data: Dict[str, Any] = _data.get("tags", {})


def tag_data() -> Dict[str, Any]:
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
