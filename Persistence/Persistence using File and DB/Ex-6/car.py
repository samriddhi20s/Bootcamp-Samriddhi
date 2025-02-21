import yaml

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def to_yaml(self):
        return yaml.dump(self.__dict__, default_flow_style=False)

    @classmethod
    def from_yaml(cls, yaml_str):
        data = yaml.load(yaml_str, Loader=yaml.SafeLoader)  # Deserialize YAML to a dictionary
        return cls(**data)  # Create a Car instance using unpacked dictionary values

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model}, year={self.year})"
