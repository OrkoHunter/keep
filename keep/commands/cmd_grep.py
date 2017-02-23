import json
import os
import re
import click
from keep import cli, utils


@click.command('grep', short_help='Searches for a saved command.')
@click.argument('pattern')
@cli.pass_context
def cli(ctx, pattern):
    """Searches for a saved command."""
    json_path = os.path.join(os.path.expanduser('~'), '.keep', 'commands.json')
    if not os.path.exists(json_path):
        click.echo('No commands to show. Add one by `keep new`.')
    else:
        FOUND = False
        for cmd, desc in json.loads(open(json_path, 'r').read()).items():
            if re.search(pattern, cmd + " :: " + desc):
                FOUND = True
                click.secho('$ ' + cmd + " :: " + desc, fg='green')
                break
            # Show if all the parts of the pattern are in one command/desc
            keywords_len = len(pattern.split())
            i_keyword = 0
            for keyword in pattern.split():
                if keyword.lower() in cmd.lower() or keyword.lower() in desc.lower():
                    FOUND = True
                    i_keyword += 1
            if i_keyword == keywords_len:
                click.secho('$ ' + cmd + " :: " + desc, fg='green')
                break
        if not FOUND:
            click.echo('No saved commands matches the pattern "{}"'.format(pattern))
