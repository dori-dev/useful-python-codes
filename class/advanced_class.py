"""Class is every things!
"""


class Battery:
    """Create a battery
    """

    def __init__(self, battery_size=1000):
        self.battery_size = battery_size

    def get_range(self, manufacturer):
        """get range of car with battery size

        Args:
            manufacturer (str): creator

        Returns:
            int: return best range
        """
        if manufacturer == 'tesla':
            return self.battery_size * 5
        return self.battery_size * 3


class Car:
    """Model a simple car"""

    def __init__(self, manufacturer: str, model: str, year: int) -> None:
        """Initialize the car class

        Args:
            manufacturer (str): manufacturer of car
            model (str): model of car
            year (int): year car made
        """
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self) -> str:
        """description of car with it information

        Returns:
            str: car description
        """
        car_desc = f"{self.manufacturer} {self.year} {self.model}"
        return car_desc.title()

    def read_odometer(self) -> None:
        """print odometer value
        """
        print(f'{self.odometer_reading} KM')

    def update_odometer(self, kilometerage: int) -> None:
        """update the odometer value

        Args:
            kilometerage (int): odometer kilometerage
        """
        if kilometerage >= 0:
            self.odometer_reading += kilometerage
        else:
            print('You can\'t roll back an odometer!')


class ElectricCar(Car):
    """a electric car subclass of car superclass
    """

    def __init__(self, manufacturer: str, model: str, year: int, battery: object):
        super().__init__(manufacturer, model, year)
        self.battery = battery
        # delattr(self, 'model')
        # delattr(Car, 'read_odometer')

    def get_battery_size(self) -> int:
        """get battery size of electric car

        Returns:
            int: return battery size
        """
        return self.battery.battery_size

    def get_best_range(self):
        """get best range of car

        Returns:
            int: best range
        """
        return self.battery.get_range(self.manufacturer)

    def get_description(self) -> str:
        """description of car with it information

        Returns:
            str: car description
        """
        car_desc = f"{self.manufacturer} {self.year} {self.model} {self.battery.battery_size}"
        return car_desc.title()


if __name__ == "__main__":
    my_battery = Battery(500)

    my_car = ElectricCar('tesla', 's4', 2020, my_battery)
    my_car.read_odometer()
    print(my_car.get_description())
    print(my_car.get_battery_size())
    print(my_car.get_best_range())

    my_car = ElectricCar('xyz', 's4', 2020, my_battery)
    print(my_car.get_battery_size())
    print(my_car.get_best_range())
