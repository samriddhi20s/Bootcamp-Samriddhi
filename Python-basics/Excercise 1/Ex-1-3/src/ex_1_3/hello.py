import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    """Greets the user."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    app()
