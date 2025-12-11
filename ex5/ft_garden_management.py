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


class HealthError(GardenError):
    """Exception raised for health errors."""

    def __init__(self, message: str):
        super().__init__(message)


class Plant:
    """Base plant."""

    def __init__(self, name: str, water_level: int, sun_hours: int):
        """Initialize a plant with name and height."""
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours


class GardenManager:
    """Manages garden"""

    def __init__(self):
        """Initialize a garden."""
        self.plants = []
        self.water_tank = 50

    def add_plant(self, plant: Plant):
        """Adds plant to garden"""
        try:
            if plant.name == "" or plant.name is None:
                raise PlantError("Plant name cannot be empty")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as exc:
            print(f"Error adding plant: {exc}")

    def water_plants(self):
        """Waters all the plants in garden"""
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant.name is None:
                    raise WaterError(f"Cannot water {plant} - invalid plant!")
                self.water_tank -= 1
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        except WaterError as exc:
            print(f"Error watering plant: {exc}")
        finally:
            print("Closing watering system")

    def check_plant_health(self):
        """Check if plant health parameters are valid"""
        try:
            for plant in self.plants:
                if plant.name == "" or plant.name is None:
                    raise HealthError("Plant name cannot be empty!")
                if plant.water_level > 10:
                    raise HealthError(
                        f"{plant.name}: Water level "
                        f"{plant.water_level} is too high (max 10)")
                if plant.water_level < 1:
                    raise HealthError(
                        f"{plant.name}: Water level "
                        f"{plant.water_level} is too low (min 1)")
                if plant.sun_hours > 12:
                    raise HealthError(
                        f"{plant.name}: Sunlight hours "
                        f"{plant.sun_hours} is too high (max 12)")
                if plant.sun_hours < 2:
                    raise HealthError(
                        f"{plant.name}: Sunlight hours "
                        f"{plant.sun_hours} is too low (min 2)")
                print(f"{plant.name}: healthy (water: "
                      f"{plant.water_level}, sun: {plant.sun_hours})")
        except HealthError as exc:
            print(f"Error checking {exc}")


def test_garden_system():
    """Test the complete garden management system"""
    print("=== Garden Management System ===\n")

    # 1. Test adding plants
    print("Adding plants to garden...")
    garden = GardenManager()
    garden.add_plant(Plant("tomato", 5, 8))
    garden.add_plant(Plant("lettuce", 14, 7))
    garden.add_plant(Plant("", 5, 6))
    print()

    # 2. Test watering plants
    print("Watering plants...")
    garden.water_plants()
    print()

    # 3. Test checking plant health
    print("Checking plant health...")
    garden.check_plant_health()
    print()

    # 4. Test error recovery with low water tank
    print("Testing error recovery...")
    try:
        garden.water_tank = 0
        if garden.water_tank < 10:
            raise GardenError("Not enough water in tank!")
    except GardenError as exc:
        print(f"Caught GardenError: {exc}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_system()
