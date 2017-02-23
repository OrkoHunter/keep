import click
from keep.cli import pass_context


@click.command('pull', short_help='Updates the local database with remote.')
@pass_context
def cli(ctx):
    """Saves a new command"""
    cmd = click.prompt('Command : ')
    desc = click.prompt('Description : ')
    print(type(cmd))
    print(type(desc))

    if ctx.verbose:
        ctx.log('Initialized the repository')
