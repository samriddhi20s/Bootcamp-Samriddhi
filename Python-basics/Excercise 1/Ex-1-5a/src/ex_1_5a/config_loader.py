import yaml
import os

def load_config(file_path=None):
    """Loads configuration from a YAML file."""
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), "../config/_config.yaml")

    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            return config if config else {}
    except FileNotFoundError:
        print("Warning: _config.yaml not found. Using default values.")
        return {}
    except yaml.YAMLError as e:
        print(f"Error loading YAML file: {e}")
        return {}
