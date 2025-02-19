import yaml
import os

# Default config path inside package
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "default_config.yaml")

def find_config_file():
    """Finds the configuration file based on priority order."""
    
    # 1️⃣ Check if _config.yaml exists in the current directory
    if os.path.exists("_config.yaml"):
        return "_config.yaml"

    # 2️⃣ Search in ATK_CONFIG_PATH environment variable directories
    env_paths = os.environ.get("ATK_CONFIG_PATH", "").split(os.pathsep)  # os.pathsep is ':' (Linux/macOS) or ';' (Windows)
    for path in env_paths:
        config_file = os.path.join(path, "_config.yaml")
        if os.path.exists(config_file):
            return config_file

    # 3️⃣ Use the default config if no other files are found
    return DEFAULT_CONFIG_PATH

def load_config():
    """Loads configuration from the found YAML file."""
    config_file = find_config_file()
    
    try:
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
            return config if config else {}  # Return empty dict if file is empty
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error loading YAML file ({config_file}): {e}")
        return {}
