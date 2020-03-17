# coding: utf-8

import click
from find_temas.find_temas_scripts import generate_temas_from_csv, get_base_as_df, get_temas, find_temas

@click.group()
def cli():
    pass

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('base', nargs=1, type=click.Path(exists=True))
@click.argument('temas', nargs=1, type=click.Path(exists=True))
@click.argument('coluna_texto', nargs=1, type=str, default="texto")
@click.argument('output', nargs=1, type=str, default="output.csv")
@click.option('--csv', default=False)
def find(base, temas, coluna_texto, output, csv):
    """
    Usage: find-temas find "base.csv" "temas.json" "texto"
    """
    click.echo(click.format_filename(base))
    click.echo(click.format_filename(temas))
    
    if csv:
        temas = generate_temas_from_csv(temas)
    else:
        temas = get_temas(temas)
    
    base_df = get_base_as_df(base, coluna_texto)

    find_temas(base_df, temas, coluna_texto, output)
    click.echo("done")

cli.add_command(find)