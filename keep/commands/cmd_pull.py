import os
import click
from keep import cli, utils


@click.command('pull', short_help='Updates the local database with remote.')
@cli.pass_context
def cli(ctx):
    """Updates the local database with remote."""
    credentials_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    if not os.path.exists(credentials_path):
        click.echo('You are not registered.')
        utils.register()
    else:
        utils.pull(ctx)
