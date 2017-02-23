import os
import shutil
import click
from keep import cli, utils

@click.command('init', short_help='Initializes the CLI.')
@cli.pass_context
def cli(ctx):
    """Initializes the CLI environment."""
    dir_path = os.path.join(os.path.expanduser('~'), '.keep')
    if os.path.exists(dir_path):
        if click.confirm('[CRITICAL] Remove everything inside ~/.keep ?', abort=True):
            shutil.rmtree(dir_path)
    utils.first_time_use(ctx)
