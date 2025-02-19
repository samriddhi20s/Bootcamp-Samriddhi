from setuptools import setup, find_packages

setup(
    name="many_hellos",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  # Ensures default_config.yaml is included
    install_requires=["PyYAML"],  # Required dependencies
    entry_points={
        "console_scripts": [
            "many-hellos=many_hellos.say_hello:main"
        ]
    },
    author="Samriddhi Chaturvedi",
    author_email="samridhichaturvedi9@gmail.com",
    description="A package that prints 'Hello' multiple times based on config.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samriddhi20s/many_hellos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
