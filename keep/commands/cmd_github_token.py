import click
import json
import os
from keep import cli
from github import Github, InputFileContent


@click.command('github_token', short_help='Register a GitHub Token to use GitHub Gists as a backup.')
@cli.pass_context
def cli(ctx):
    """Register a GitHub Token to use GitHub Gists as a backup."""

    dir_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    existing_token = None
    if os.path.exists(dir_path):
        with open(dir_path) as f:
            existing_token = json.load(f)

        if click.confirm('[CRITICAL] Reset token saved in ~/.keep/.credentials ?',
                         abort=True):
            os.remove(dir_path)

    token = click.prompt('Create a GITHUB TOKEN with permission to Gists and paste here ')
    gist_id = existing_token.get('gist') if existing_token else None
    click.echo("\nAwesome! Your GitHub token has been registered. Now, we need a GIST ID to store the commands in keep.")
    prompt_str = 'If you already have a GitHub Gist created by keep, paste the GIST ID here, or else press Enter (we will create a Gist for you). '
    new_gist_id = click.prompt(prompt_str, default='', show_default=False)

    if new_gist_id:
        gist_id = new_gist_id

    if not gist_id:
        g = Github(token)
        gist = g.get_user().create_gist(False,
                                        files={'commands.json': InputFileContent('{}')},
                                        description='Backup for keep - https://github.com/OrkoHunter/keep')
        gist_id = gist.id

    with open(dir_path, 'w') as f:
        json.dump({'token': token, 'gist': gist_id}, f)

    click.echo("Done! Gist URL - https://gist.github.com/" + gist_id)
    click.echo("Your token and gist ID has been stored inside ~/.keep/.credentials")
    click.echo("You can now use `keep push` or `keep pull`")