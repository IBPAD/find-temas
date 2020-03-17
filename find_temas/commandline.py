# coding: utf-8

import click
from find_temas.find_temas_scripts import find_temas

@click.group()
def cli():
    pass

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('base', nargs=1, type=click.Path(exists=True))
@click.argument('temas', nargs=1, type=click.Path(exists=True))
@click.argument('coluna_texto', nargs=1, type=str)
def find(base, temas, coluna_texto):
    """
    Usage: find-temas find "base.csv" "temas.json" "texto"
    """
    click.echo(click.format_filename(base))
    click.echo(click.format_filename(temas))
    find_temas(base, temas, coluna_texto)
    click.echo("done")

cli.add_command(find)