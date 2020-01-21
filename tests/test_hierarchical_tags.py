# -*- coding: utf-8 -*-

# Hierarchical Tags 2 for Anki
#
# Copyright (C) 2020  Aristotelis P. <https//glutanimate.com/>
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

from pytest_anki import profile_loaded, AnkiSession, local_addon_config
import pytest
from pathlib import Path
import json


config_path = Path(__file__).parent.parent / "src" / "hierarchical_tags" / "config.json"
defaults = json.loads(config_path.read_text(encoding="utf-8"))


@pytest.mark.forked
def test_ui_throws_errors(anki_session: AnkiSession):
    with local_addon_config(anki_session.base, "hierarchical_tags", defaults):
        with profile_loaded(anki_session.mw):
            import hierarchical_tags  # noqa: F401
            import aqt

            browser = aqt.dialogs.open("Browser", anki_session.mw)
            browser.close()
