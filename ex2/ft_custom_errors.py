#!/usr/bin/env python3

class GardenError(Exception):
    """Exception raised for garden errors."""

    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for plant errors."""

    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for water errors."""

    def __init__(self, message: str):
        super().__init__(message)


def test_error_types():
    """Test different error types"""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        wilting = True
        if wilting:
            raise PlantError("The tomato is wilting!")
    except PlantError as err_message:
        print(f"Caught a PlantError: {err_message}\n")

    print("Testing WaterError...")
    try:
        water = 10
        if water < 50:
            raise WaterError("Not enough water in the tank!")
    except WaterError as err_message:
        print(f"Caught a WaterError: {err_message}\n")

    print("Testing catching all garden errors...")
    try:
        wilting = True
        if wilting:
            raise PlantError("The tomato is wilting!")
    except GardenError as err_message:
        print(f"Caught a garden error: {err_message}")
    try:
        water = 10
        if water < 50:
            raise WaterError("Not enough water in the tank!")
    except GardenError as err_message:
        print(f"Caught a garden error: {err_message}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
