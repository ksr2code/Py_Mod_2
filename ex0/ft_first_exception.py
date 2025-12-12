#!/usr/bin/env python3

def check_temperature(temp_str: str):
    """Validate temperature input"""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            return temp
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """Testing the temperature validation with different values"""
    print("=== Garden Temperature Checker ===\n")
    test_values = ["25", "abc", "100", "-50"]
    for value in test_values:
        print(f"Testing temperature: {value}")
        if check_temperature(value) is not None:
            print(f"Temperature {value}°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
