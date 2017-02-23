import json
import os
import re
import click
from keep import cli, utils


@click.command('run', short_help='Executes a saved command.')
@click.argument('pattern')
@cli.pass_context
def cli(ctx, pattern):
    """Executes a saved command."""
    json_path = os.path.join(os.path.expanduser('~'), '.keep', 'commands.json')
    if not os.path.exists(json_path):
        click.echo('No commands to run. Add one by `keep new`.')
    else:
        FOUND = False
        for cmd, desc in json.loads(open(json_path, 'r').read()).items():
            if re.search(pattern, cmd + " :: " + desc):
                FOUND = True
                if click.confirm("Execute\n\n\t{}\n\n\n?".format(cmd), default=True):
                    os.system(cmd)
                    break
            # Execute if all the parts of the pattern are in one command/desc
            keywords_len = len(pattern.split())
            i_keyword = 0
            for keyword in pattern.split():
                if keyword.lower() in cmd.lower() or keyword.lower() in desc.lower():
                    FOUND = True
                    i_keyword += 1
            if i_keyword == keywords_len:
                if click.confirm("Execute\n\n\t{}\n\n\n?".format(cmd), default=True):
                    os.system(cmd)
                    break
        if not FOUND:
            click.echo('No saved commands matches the pattern "{}"'.format(pattern))
