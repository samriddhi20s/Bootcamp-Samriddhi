from setuptools import setup, find_packages

setup(
    name="hello-cli",
    version="0.1.0",
    packages=find_packages(where="source"),
    package_dir={"": "source"},
    install_requires=["typer"],
    entry_points={
        "console_scripts": [
            "hello=hello:app"
        ],
    },
)
