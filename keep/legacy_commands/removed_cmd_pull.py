import os
import click
from keep import cli, utils


@click.command('pull', short_help='Updates the local database with remote.')
@click.option('--overwrite', is_flag=True, help='Overwrite local commands')
@cli.pass_context
def cli(ctx, overwrite):
    """Updates the local database with remote."""
    credentials_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    if not os.path.exists(credentials_path):
        click.echo('You are not registered.')
        utils.register()
    else:
        utils.pull(ctx, overwrite)
