#!/usr/bin/env python3

def water_plants(plant_list):
    """Water plants with automatic cleanup"""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is not None:
                print(f"Watering {plant}")
            else:
                plant = 1 / 0
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test watering system with good and bad inputs"""
    good_plant_list = ["tomato", "lettuce", "carrots"]
    bad_plant_list = ["tomato", None, "carrots"]
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(good_plant_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
