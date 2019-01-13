import os
import click
from keep import cli, utils


@click.command('push', short_help='Pushes the local database to remote.')
@cli.pass_context
def cli(ctx):
    """Pushes the local database to remote."""
    credentials_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    if not os.path.exists(credentials_path):
        click.echo('You are not registered.')
        utils.register()
    else:
        utils.push(ctx)
