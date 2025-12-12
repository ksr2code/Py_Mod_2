#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if plant health parameters are valid"""
    try:
        if plant_name == "" or plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as exc:
        print(f"Error: {exc}")


def test_plant_checks():
    """Test plant health checks with various inputs"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 5, 6)
    print()
    print("Testing empty plant name...")
    check_plant_health("", 5, 6)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 6)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
