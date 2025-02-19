import typer
from helloworld import say_hello

app = typer.Typer()

@app.command()
def hello(names: list[str]):
    """Print hello for each name."""
    for name in names:
        typer.echo(say_hello(name))

if __name__ == "__main__":
    app()