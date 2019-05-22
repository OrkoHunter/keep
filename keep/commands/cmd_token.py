import click
import json
import os
from keep import cli
from github import Github, InputFileContent


@click.command('token', short_help='Register github gist token')
@cli.pass_context
def cli(ctx):
    """Store Github gist token"""

    dir_path = os.path.join(os.path.expanduser('~'), '.keep', '.credentials')
    existing_token = None
    if os.path.exists(dir_path):

        with open(dir_path) as f:
            existing_token = json.load(f)

        if click.confirm('[CRITICAL] Reset credentials saved in ~/.keep/.credentials ?',
                         abort=True):
            os.remove(dir_path)

    token = click.prompt('Token')
    gist_id = existing_token.get('gist') if existing_token else None
    new_gist_id = click.prompt('Existing gist id?', default='', show_default=False)

    if new_gist_id:
        gist_id = new_gist_id

    if not gist_id:
        g = Github(token)
        gist = g.get_user().create_gist(False,
                                        files={'commands.json': InputFileContent('{}')},
                                        description='keep - meta cli toolkit')
        gist_id = gist.id

    with open(dir_path, 'w') as f:
        json.dump({'token': token, 'gist': gist_id}, f)
