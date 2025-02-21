import yaml

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def to_yaml(self):
        """Convert the Car object to a YAML string."""
        return yaml.dump(self.__dict__, default_flow_style=False)

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model}, year={self.year})"
