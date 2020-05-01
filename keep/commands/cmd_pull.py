import click
import os
from keep import cli, utils
from github import Github


@click.command('pull', short_help='Pull commands from saved GitHub gist.')
@cli.pass_context
def cli(ctx):
    """Pull commands from saved GitHub gist."""

    commands_file_path = os.path.join(utils.dir_path, 'commands.json')
    token = utils.get_github_token()
    if not token:
        return

    hub = Github(token['token'])
    gist = hub.get_gist(token['gist'])

    gist_url = f"https://gist.github.com/{token['gist']}"
    prompt_str = f"[CRITICAL] Replace local commands with GitHub gist\nGist URL : {gist_url} ?"
    if click.confirm(prompt_str, abort=True):
        pass

    """Using `w+` so it create the file if doesn't exist (Issue #64)"""
    with open(commands_file_path, 'w+') as commands_file:
        commands_file.write(gist.files['commands.json'].content)
    click.echo("Done!")
