#Contracts with @property: Implement a Temperature class that strictly controls setting and getting temperature values using @property.
#Enforce a range for temperature values (e.g., -273.15°C to 5000°C)
class Temperature:
    def __init__(self, temp=0):
        self._temp = temp

    @property
    def temp(self):
        """Getter for the temperature value."""
        return self._temp

    @temp.setter
    def temp(self, value):
        """Setter for the temperature value, enforcing the range."""
        if -273.15 <= value <= 5000:
            self._temp = value
        else:
            raise ValueError("Temperature must be between -273.15°C and 5000°C.")

# Testing the Temperature class
try:
    t1 = Temperature(25)
    print(f"Temperature is: {t1.temp}°C")  # output 25

    t1.temp = 300
    print(f"Updated temperature is: {t1.temp}°C")  # output 300

    t1.temp = -300  # Invalid temperature
except ValueError as e:
    print(e)  # raise an error

