import os
import click
from keep import cli, utils

@click.command('register', short_help='Register user over server.')
@cli.pass_context
def cli(ctx):
    """Initializes the CLI environment."""
    dir_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    if os.path.exists(dir_path):
        if click.confirm('[CRITICAL] Reset credentials saved in ~/.keep/.credentials ?', abort=True):
            os.remove(dir_path)
    utils.register()
