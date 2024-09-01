
import pytest
import guess_number as gn

def test_guess_correct():
    assert gn.check_guess(50, 50) == "BINGO!!"

def test_guess_higher():
    assert gn.check_guess(50, 40) == "guess higher"

def test_guess_lower():
    assert gn.check_guess(50, 60) == "guess lower"

def test_guess_str_error():
    with pytest.raises(ValueError, match="ValueError"):
        gn.check_guess(50, "forty-two")

def test_guess_outofrange():
    with pytest.raises(ValueError, match="number out of range"):
        gn.check_guess(50, 144)

def test_guess_negative():
    with pytest.raises(ValueError, match="number out of range"):
        gn.check_guess(50, -50)
