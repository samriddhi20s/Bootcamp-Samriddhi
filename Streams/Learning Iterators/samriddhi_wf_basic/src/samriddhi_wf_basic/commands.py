import typer
from samriddhi_wf_basic import processing_functions

app = typer.Typer()

@app.command()
def upper_case(input_filename: str, output_filename: str = None):
    """Convert file text to uppercase."""
    processing_functions.upper_case(input_filename, output_filename)

@app.command()
def lower_case(input_filename: str, output_filename: str = None):
    """Convert file text to lowercase."""
    processing_functions.lower_case(input_filename, output_filename)

@app.command()
def capitalize(input_filename: str, output_filename: str = None):
    """Capitalize all words in a file."""
    processing_functions.capitalize(input_filename, output_filename)

@app.command()
def remove_stop_words(text: str):
    """Remove common stop words from a text string."""
    print(processing_functions.remove_stop_words(text))

@app.command()
def fetch_geo_ip(ip: str):
    """Fetch geographic info for an IP address."""
    print(processing_functions.fetch_geo_ip(ip))

@app.command()
def uk_to_us(text: str):
    """Convert UK spelling to US spelling."""
    print(processing_functions.uk_to_us(text))

if __name__ == "__main__":
    app()

