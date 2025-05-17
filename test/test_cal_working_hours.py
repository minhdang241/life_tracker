from __future__ import annotations

import json

from calc_working_time import calculate_working_time


def test_calculate_working_time():
    with open("tests/test.json") as f:
        data = json.load(f)
    assert calculate_working_time(data) == 7.25
