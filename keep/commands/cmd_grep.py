import click
from keep.cli import pass_context


@click.command('grep', short_help='Searches for a saved command.')
@pass_context
def cli(ctx):
    """Saves a new command"""
    cmd = click.prompt('Command : ')
    desc = click.prompt('Description : ')
    print(type(cmd))
    print(type(desc))

    if ctx.verbose:
        ctx.log('Initialized the repository')
