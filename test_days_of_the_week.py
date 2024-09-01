import pytest
import days_of_the_week as dotw

def test_sunday():
    assert dotw.day_of_the_week(1) == 'Sunday'

def test_monday():
    assert dotw.day_of_the_week(2) == 'Monday'

def test_tuesday():
    assert dotw.day_of_the_week(3) == 'Tuesday'

def test_wednesday():
    assert dotw.day_of_the_week(4) == 'Wednesday'

def test_thursday():
    assert dotw.day_of_the_week(5) == 'Thursday'

def test_friday():
    assert dotw.day_of_the_week(6) == 'Friday'

def test_saturday():
    assert dotw.day_of_the_week(7) == 'Saturday'

def test_invalid_input():
    with pytest.raises(ValueError):
        dotw.day_of_the_week(0)

    with pytest.raises(ValueError):
        dotw.day_of_the_week(8)
