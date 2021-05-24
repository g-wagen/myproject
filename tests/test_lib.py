from myproject.lib import try_me, rgb_to_float

def test_try_me_return():
    assert type(try_me()) == str

def test_rgb_to_float_negative():
    assert rgb_to_float(-5, 5, 20) == None

def test_rgb_to_float_return():
    assert type(rgb_to_float(255, 255, 255)) == tuple
    assert len(rgb_to_float(255, 255, 255)) == 3

def test_rgb_to_float_return():
    assert type(rgb_to_float(255, 255, 255)[0]) == float
    assert type(rgb_to_float(255, 255, 255)[1]) == float
    assert type(rgb_to_float(255, 255, 255)[2]) == float

def test_rgb_to_float_max():
    assert rgb_to_float(255, 255, 255) == (1.0, 1.0, 1.0)

def test_rgb_to_float_min():
    assert rgb_to_float(0, 0, 0) == (0.0, 0.0, 0.0)
