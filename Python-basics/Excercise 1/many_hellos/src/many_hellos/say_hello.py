from many_hellos.config_loader import load_config

def say_hello(name):
    """Returns a greeting message repeated based on num_times from config."""
    config = load_config()
    num_times = config.get("num_times", 1)  # Default to 1 if not found
    return (f"Hello, {name}!\n" * num_times).strip()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Prints 'Hello' multiple times.")
    parser.add_argument("name", type=str, help="Name to greet")
    args = parser.parse_args()
    
    print(say_hello(args.name))
