import pytest
from working import convert

def test_proper_use():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8:30 AM to 10:30 AM") == "08:30 to 10:30"

def test_incorect_use():
    with pytest.raises(ValueError):
        convert("9 AM to 17:00")

def test_smt():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_corner_case():
    with pytest.raises(ValueError):
        convert("90 AM to 5 PM")
