import click
import os
from keep import cli, utils
from github import Github


@click.command('download', short_help='Download commands from github gist')
@cli.pass_context
def cli(ctx):
    """Download commands from github gist"""

    commands_file_path = os.path.join(utils.dir_path, 'commands.json')
    token = utils.get_github_token()
    if not token:
        return

    if click.confirm('[CRITICAL] Reset commands saved with ones from Gist?', abort=True):
        os.remove(commands_file_path)

    hub = Github(token['token'])
    gist = hub.get_gist(token['gist'])
    with open(commands_file_path, 'w') as commands_file:
        commands_file.write(gist.files['commands.json'].content)
