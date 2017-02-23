import os
import click
from keep import cli, utils


@click.command('list', short_help='Show the saved commands.')
@cli.pass_context
def cli(ctx):
    """Show the saved commands."""
    json_path = os.path.join(os.path.expanduser('~'), '.keep', 'commands.json')
    if not os.path.exists(json_path):
        click.echo('No commands to show. Add one by `keep new`.')
    else:
        utils.list_commands(ctx)
