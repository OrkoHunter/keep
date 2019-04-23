import click
import json
from keep import cli, utils
from github import Github, InputFileContent


@click.command('upload', short_help='Upload commands to github gist')
@cli.pass_context
def cli(ctx):
    """Upload commands to github gist"""

    token = utils.get_github_token()
    if not token:
        return

    click.confirm('[CRITICAL] Reset commands saved in Gist with ones locally?', abort=True)

    commands = utils.read_commands()
    if not commands:
        click.echo("No commands to edit, Add one by 'keep new'. ")
    else:
        hub = Github(token['token'])
        gist = hub.get_gist(token['gist'])
        gist.edit(files={'commands.json': InputFileContent(json.dumps(commands))})
