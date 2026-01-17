from leap_year import leap
def test_leap_year():
    assert leap("2028")=="yes"
def test_not_leap_year():
    assert leap("1900")=="no"
def test_leap_not_a_year():
    assert leap("2000")=="yes"