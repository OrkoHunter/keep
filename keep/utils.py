"""Utility functions of the cli."""
import json
import os
import random
import string
import sys
import time
import click
import requests

def save_command(cmd, desc):

    pass


def log(ctx, message):
    """Prints log when verbose set to True."""
    if ctx.verbose:
        ctx.log(message)

def first_time_use(ctx):
    click.secho("Hello ! Thank you for installing Keep", bold=True, fg='cyan')
    click.secho("Initializing environment in ~/.keep directory", fg='green')
    for i in range(2):
        click.echo('.', nl=False)
        time.sleep(0.5)
    click.echo('.OK', nl=True)
    dir_path = os.path.join(os.path.expanduser('~'), '.keep')
    os.mkdir(dir_path)
    if click.confirm('Proceed to register?', abort=True, default=True):
        click.echo("Your credentials will be saved in the ~/.keep directory.")
        email = click.prompt('Email', confirmation_prompt=True)
        json_res = {
            'email': email
        }
        click.echo('Verifying with existing users...')
        r = requests.post('https://keep-cli.herokuapp.com/check-user', json=json_res)
        if r.json()['exists']:
            click.secho('User already exists !', fg='red')
            email = click.prompt('Email', confirmation_prompt=True)
            json_res = {
                'email': email
            }
            r = requests.post('https://keep-cli.herokuapp.com/check-user', json=json_res)
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(255))
        credentials_file = os.path.join(dir_path, '.credentials')
        credentials = {
            'email': email,
            'password': password
        }
        with open(credentials_file, 'w+') as f:
            f.write(json.dumps(credentials))
        click.secho("Generated password for " + email, fg='cyan')
        click.secho(password, fg='cyan')
        click.echo("Registering new user ...")
        json_res = {
            'email': email,
            'password': password
        }
        r = requests.post('https://keep-cli.herokuapp.com/register', json=json_res)
        if r.status_code == 200:
            click.secho("User successfully registered !", fg='green')
        click.secho("Credentials file saved at ~/.keep/.credentials", fg='green')
    sys.exit(0)

