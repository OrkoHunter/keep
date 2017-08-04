import click
from keep import cli, utils

@click.command('new', short_help='Saves a new command.')
@cli.pass_context
def cli(ctx):
    """Saves a new command"""
    cmd = click.prompt('Command')
    desc = click.prompt('Description ')
    alias = click.prompt('Alias (optional)', default='')
    utils.save_command(cmd, desc, alias)

    utils.log(ctx, 'Saved the new command - {} - with the description - {}.'.format(cmd, desc))
