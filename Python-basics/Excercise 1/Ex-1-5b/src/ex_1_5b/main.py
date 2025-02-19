from config_loader import load_config

def say_hello(name):
    """Returns a greeting message repeated based on config."""
    config = load_config()
    num_times = config.get("num_times", 1)  # Default to 1 if not found
    return (f"Hello, {name}!\n" * num_times).strip()

if __name__ == "__main__":
    print(say_hello("Alice"))
