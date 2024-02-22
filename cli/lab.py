import click

@click.group()
def cli():
    """CLI for interacting with labrador"""
    pass

@cli.command()
def help():
    """Provides more information about commands"""
    click.echo("# help TBD")

@cli.command()
def init():
    """Initializes environment for labrador"""
    click.echo("# init TBD")

@cli.command()
def generate():
    """Generates ..."""
    click.echo("# generate TBD")

@cli.command()
def train():
    """Trains labrador model"""
    click.echo("# train TBD")

@cli.command()
def test():
    """Perform rudimentary tests of the model"""
    click.echo("# test TBD")

@cli.command()
def chat():
    """Run a chat using the modified model"""
    click.echo("# chat TBD")