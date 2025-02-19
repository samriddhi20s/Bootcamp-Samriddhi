import yaml
import os

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "default_config.yaml")

def find_config_file():
    """Search for the config file in the current directory, CONFIG_PATH env variable, or use default."""
    
    # Check current directory
    if os.path.exists("_config.yaml"):
        return "_config.yaml"

    # Check CONFIG_PATH environment variable
    config_paths = os.environ.get("CONFIG_PATH", "").split(":")
    for path in config_paths:
        config_file = os.path.join(path, "_config.yaml")
        if os.path.exists(config_file):
            return config_file

    # Fall back to default config
    return DEFAULT_CONFIG_PATH

def load_config():
    """Loads configuration from the found YAML file."""
    config_file = find_config_file()
    
    try:
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
            return config if config else {}
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error loading YAML file ({config_file}): {e}")
        return {}
