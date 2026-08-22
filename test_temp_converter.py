from temp_converter import TemparatureConverter

def test_celsius_to_fahrenheit():
    converter = TemparatureConverter("Test")
    result = converter.celsius_to_fahrenheit(0)
    assert result == 32

def test_fahrenheit_to_celsius_negative():
    converter = TemparatureConverter("Test")
    result = converter.fahrenheit_to_celsius(-40)
    assert result == -40

def test_fahrenheit_to_celsius():
    converter = TemparatureConverter("Test")
    result = converter.fahrenheit_to_celsius(32)
    assert result == 0, f"Expected 0 but got {result}"

def test_fahrenheit_to_celsius_hand_calculated():
    converter = TemparatureConverter("Test")
    result = converter.celsius_to_fahrenheit(56)
    assert round(result, 1) == 132.8