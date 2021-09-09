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
from typing import Dict, Literal, TypedDict

ALL_ADDONS_PATH = Path(__file__).parent.parent.absolute()
ADDON_PATH = ALL_ADDONS_PATH / __package__


class TagState(TypedDict, total=False):
    pin: bool
    color: str  # HTML code


TagDataType = Dict[str, TagState]
UserDataType = Dict[Literal["tags"], TagDataType]


class UserData:

    _data_path = ADDON_PATH / "user_files" / "data.json"
    _bettertags_data_path = ALL_ADDONS_PATH / "bettertags" / "user_files" / "data.json"

    def __init__(self):
        self.tags: TagDataType = {}
        if not self._data_path.exists():
            # Initial run
            if not self._data_path.parent.exists():
                self._data_path.parent.mkdir(exist_ok=True)
            if self._bettertags_data_path.exists():
                self._migrate_from_bettertags()
            self.save()
        self.read()

    def read(self):
        try:
            with self._data_path.open(encoding="UTF-8") as data_file:
                data: UserDataType = json.load(data_file)
        except Exception as e:
            print(e)
            data = {}
        self.tags = data.get("tags", {})

    def save(self):
        data: UserDataType = {"tags": self.tags}
        with self._data_path.open(mode="w", encoding="UTF-8") as data_file:
            data_file.write(json.dumps(data))

    def _migrate_from_bettertags(self):
        with self._bettertags_data_path.open() as data_file:
            bettertags_data = json.load(data_file)
        bettertags_tag_state_data = bettertags_data.get("tagState", {})

        tag_data = self.tags

        for tag, state in bettertags_tag_state_data.items():
            pinned_state = state.get("pinned")
            color_state = state.get("color")

            if pinned_state is None and color_state is None:
                continue

            if tag not in tag_data:
                tag_data[tag] = {}  # type: ignore
            if pinned_state == 1:
                tag_data[tag]["pin"] = True
            if color_state:
                tag_data[tag]["color"] = color_state


user_data = UserData()
