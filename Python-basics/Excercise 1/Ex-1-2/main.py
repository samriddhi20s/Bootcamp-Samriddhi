import typer
from hello import say_hello

app = typer.Typer()

@app.command()
def hello(name: str):
    """Command that prints a hello message."""
    typer.echo(say_hello(name))

if __name__ == "__main__":
    app()
