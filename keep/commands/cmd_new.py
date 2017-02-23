import click
from keep import cli, utils

@click.command('new', short_help='Saves a new command.')
@cli.pass_context
def cli(ctx):
    """Saves a new command"""
    cmd = click.prompt('Command : ')
    desc = click.prompt('Description : ')
    utils.save_command(cmd, desc)

    utils.log(ctx, 'Initialized the repository')
