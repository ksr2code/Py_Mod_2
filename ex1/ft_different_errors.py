def garden_operations(operation_type: str):
    """Demonstrate different error types"""
    plant_dict = {"tomato": "healthy", "lettuce": "growing"}

    if operation_type == "ValueError":
        try:
            num = int("abc")
            print(num)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")

    elif operation_type == "ZeroDivisionError":
        try:
            result = 100 / 0
            print(result)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")

    elif operation_type == "FileNotFoundError":
        try:
            open("missing.txt")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    elif operation_type == "KeyError":
        try:
            value = plant_dict["missing_plant"]
            print(value)
        except KeyError:
            print("Caught KeyError: 'missing_plant'\n")

    elif operation_type == "multiple":
        try:
            num = int("abc")
        except (ValueError, ZeroDivisionError, KeyError):
            print("Caught an error, but program continues!\n")


def test_error_types():
    """Test different error types"""
    print("=== Garden Error Types Demo\n ===")
    print("Testing ValueError...")
    garden_operations("ValueError")

    print("Testing ZeroDivisionError...")
    garden_operations("ZeroDivisionError")

    print("Testing FileNotFoundError...")
    garden_operations("FileNotFoundError")

    print("Testing KeyError...")
    garden_operations("KeyError")

    print("Testing multiple errors together...")
    garden_operations("multiple")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
