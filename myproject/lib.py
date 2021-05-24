def try_me():
    return "You tried, amazing!"

def rgb_to_float(r,g,b):
    """
    Converts RGB to float.
    
    r = red, g = green, b = blue
    """
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        return r/255.0, g/255.0, b/255.0
