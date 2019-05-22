import click
import json
from keep import cli, utils
from github import Github, InputFileContent


@click.command('push', short_help='Push commands to a secret GitHub gist.')
@cli.pass_context
def cli(ctx):
    """Push commands to a secret GitHub gist."""

    token = utils.get_github_token()
    if not token:
        return


    gist_url = f"https://gist.github.com/{token['gist']}"
    prompt_str = f"[CRITICAL] Overwrite upstream gist with local commands?\nGist URL : {gist_url}"
    click.confirm(prompt_str, abort=True)

    commands = utils.read_commands()
    if not commands:
        click.echo("No commands to push. Add one by 'keep new'. ")
    else:
        hub = Github(token['token'])
        gist = hub.get_gist(token['gist'])
        gist.edit(files={'commands.json': InputFileContent(json.dumps(commands))})
        click.echo("Done!")