# Basic Drills in Python

## Overview
This project is a set of basic exercises designed to understand the ways of working in Python. The tasks focus on creating libraries, command-line programs, configuration management, and logging.

## Tasks Performed

### 1. Create a "Hello World" Project
- Developed a Python module that exports a function `say_hello(name: str) -> str`.
- The function returns a greeting message: `"Hello, {name}!"`.

### 2. Create a Command-Line Interface (CLI)
- Used `typer` to create a CLI named `hello`.
- Created a `main.py` file that imports the `say_hello` function.
- The command takes a name as an argument and prints the greeting message.

### 3. Publish the Library
- Packaged and published the library along with the CLI to `dev-pypi`.

### 4. Create a "Many-Hellos" Project
- Created another project `many-hellos`.
- Developed a CLI (using `typer`) that imports `helloworld.say_hello`.
- The CLI takes multiple names as arguments and prints a greeting for each name.

### 5. Extend Library with Configuration Support
- Extended the `say_hello` function to load a `_config.yaml` file.
- The YAML file contains a parameter `num_times`, which determines how many times the greeting should be repeated.
- Implemented a search mechanism for the YAML file:
  1. First, look for `_config.yaml` in the current directory.
  2. If not found, search in the paths defined by the `CONFIG_PATH` environment variable (colon `:` separated).
  3. If still not found, use a default YAML file shipped with the module.

### 6. Encapsulate Configuration Handling
- Moved configuration loading logic to a separate module.
- Updated `say_hello` to use the encapsulated config loader.
- Packaged and republished the updated library.

### 7. Test with `many-hellos` CLI
- Tested by placing a `_config.yaml` file in the current working directory.
- Tested using the `CONFIG_PATH` environment variable.
- Tested without any config file to ensure it falls back to the default configuration.

### 8. Add Logging
- Integrated the `logging` module into both `say_hello` and the config loader.
- Enabled and disabled logging selectively to observe its effect.
- Configured logging in `many-hellos`:
  - Turned logging ON for debugging.
  - Turned logging OFF to test silent execution.
  - Turned logging ON selectively for the config reader module.

## Development Guidelines
**Rule of Thumb:** Any code written in this project should be one or more of the following:
- A **library**
- A **command-line program**
- A **Jupyter notebook**
- A **web application**

## Installation and Usage
### Installing the Library
```
pip install --index-url https://test.pypi.org/simple/ helloworld
```

### Running the CLI
#### `hello` command:
```
hello John
```

#### `many-hellos` command:
```
many-hellos Alice Bob Charlie
```

### Configuring `num_times`
- Place `_config.yaml` in the working directory with:
```yaml
num_times: 3
```
- Or set an environment variable:
```
export CONFIG_PATH=/path/to/config
```

## Logging Example
To enable logging while running `many-hellos`:
```
export LOG_LEVEL=DEBUG
many-hellos Alice Bob
```

To disable logging:
```
export LOG_LEVEL=ERROR
```

## Conclusion
This project covers:
- Python module development
- CLI creation with `typer`
- Configuration management using YAML
- Logging and debugging techniques
- Packaging and publishing libraries to `dev-pypi`

It provides hands-on experience with best practices in Python development.

