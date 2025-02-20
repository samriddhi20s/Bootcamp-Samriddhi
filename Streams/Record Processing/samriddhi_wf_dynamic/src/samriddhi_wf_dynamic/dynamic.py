import typer

app = typer.Typer()

@app.command()
def run_pipeline(input_file: str, output_file: str, config_file: str):
    typer.echo(f"Processing {input_file} -> {output_file} using {config_file}")

if __name__ == "__main__":
    app()

