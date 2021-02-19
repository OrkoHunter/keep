"""Utility functions of the cli."""
import datetime
import json
import os
import re
import random
import string
import sys
import time
import click
import requests
from terminaltables import AsciiTable
from textwrap import wrap

from keep import about

# Directory for Keep files
dir_path = os.path.join(os.path.expanduser('~'), '.keep')
# URL for the API
api_url = 'https://keep-cli.herokuapp.com'


def check_update(ctx, forced=False):
    """
    Check for update on pypi. Limit to 1 check per day if not forced
    """
    try:
        if ctx.update_checked and not forced:
            return
    except AttributeError:
        update_check_file = os.path.join(dir_path, 'update_check.txt')
        today = datetime.date.today().strftime("%m/%d/%Y")
        if os.path.exists(update_check_file):
            date = open(update_check_file, 'r').read()
        else:
            date = []
        if forced or today != date:
            ctx.update_checked = True
            date = today
            with open(update_check_file, 'w') as f:
                f.write(date)
            r = requests.get("https://pypi.org/pypi/keep/json").json()
            version = r['info']['version']
            curr_version = about.__version__
            if version > curr_version:
                click.secho("Keep seems to be outdated. Current version = "
                            "{}, Latest version = {}".format(curr_version, version) +
                            "\n\nPlease update with ", bold=True, fg='red')
                click.secho("\tpip3 --no-cache-dir install -U keep==" + str(version), fg='green')
                click.secho("\n\n")


def first_time_use(ctx):
    click.secho("Detected fresh installation. Initializing environment in ~/.keep directory", fg='green')
    for _ in range(2):
        click.echo('.', nl=False)
        time.sleep(0.5)
    click.echo('.OK', nl=True)

    os.mkdir(dir_path)

    # register()
    sys.exit(0)


def list_commands(ctx):
    table_data = [['Command', 'Description', 'Alias']]
    no_of_columns = len(table_data[0])

    commands = read_commands()
    for cmd, fields in commands.items():
        table_data.append(['$ ' + cmd, fields['desc'], fields['alias']])

    table = AsciiTable(table_data)
    max_width = table.table_width//3

    for i in range(len(table_data) - 1):
        for j in range(no_of_columns):
            data = table.table_data[i + 1][j]
            if len(data) > max_width:
                table.table_data[i + 1][j] = '\n'.join(wrap(data, max_width))

    table.inner_row_border = True
    print(table.table)


def log(ctx, message):
    """Prints log when verbose set to True."""
    if ctx.verbose:
        ctx.log(message)


# def push(ctx):
#     credentials_file = os.path.join(dir_path, '.credentials')
#     credentials = json.loads(open(credentials_file, 'r').read())
#     json_path = os.path.join(dir_path, 'commands.json')
#     credentials['commands'] = open(json_path).read()
#     url = api_url + '/push'
#     if click.confirm("This will overwrite the saved "
#                      "commands on the server. Proceed?", default=True):
#         r = requests.post(url, json=credentials)
#         if r.status_code == 200:
#             click.echo("Server successfully updated.")


# def pull(ctx, overwrite):
#     credentials_file = os.path.join(dir_path, '.credentials')
#     credentials = json.loads(open(credentials_file, 'r').read())
#     json_path = os.path.join(dir_path, 'commands.json')
#     url = api_url + '/pull'

#     r = requests.post(url, json=credentials)
#     if r.status_code == 200:
#         commands = json.loads(r.json()['commands'])

#     if not overwrite:
#         my_commands = read_commands()
#         commands.update(my_commands)

#     if not overwrite or (
#         overwrite and click.confirm(
#             "This will overwrite the locally saved commands. Proceed?", default=True)):
#             with open(json_path, 'w') as f:
#                 f.write(json.dumps(commands))
#             click.echo("Local database successfully updated.")


# def register():

#     if not os.path.exists(dir_path):
#         click.secho("\n[CRITICAL] {0} does not exits.\nPlease run 'keep init',"
#                     " and try registering again.\n".format(dir_path),
#                     fg="red", err=True)
#         sys.exit(1)

#     # User may not choose to register and work locally.
#     # Registration is required to push the commands to server
#     if click.confirm('Proceed to register?', abort=True, default=True):
#         # Verify for existing user
#         click.echo("Your credentials will be saved in the ~/.keep directory.")
#         email = click.prompt('Email', confirmation_prompt=True)
#         json_res = {'email': email}
#         click.echo('Verifying with existing users...')
#         r = requests.post('https://keep-cli.herokuapp.com/check-user', json=json_res)
#         if r.json()['exists']:
#             click.secho('User already exists !', fg='red')
#             email = click.prompt('Email', confirmation_prompt=True)
#             json_res = {'email': email}
#             r = requests.post('https://keep-cli.herokuapp.com/check-user', json=json_res)
#         # Generate password for the user
#         chars = string.ascii_letters + string.digits
#         password = ''.join(random.choice(chars) for _ in range(255))
#         credentials_file = os.path.join(dir_path, '.credentials')
#         credentials = {
#             'email': email,
#             'password': password
#         }
#         click.secho("Generated password for " + email, fg='cyan')
#         # Register over the server
#         click.echo("Registering new user ...")
#         json_res = {
#             'email': email,
#             'password': password
#         }
#         r = requests.post('https://keep-cli.herokuapp.com/register', json=json_res)
#         if r.status_code == 200:
#             click.secho("User successfully registered !", fg='green')
#             # Save the credentials into a file
#             with open(credentials_file, 'w+') as f:
#                 f.write(json.dumps(credentials))
#             click.secho(password, fg='cyan')
#             click.secho("Credentials file saved at ~/.keep/.credentials.json", fg='green')
#     sys.exit(0)


def remove_command(cmd):
    commands = read_commands()
    if cmd in commands:
        del commands[cmd]
        write_commands(commands)
    else:
        click.echo('Command - {} - does not exist.'.format(cmd))


def save_command(cmd, desc, alias=""):
    json_path = os.path.join(dir_path, 'commands.json')
    commands = {}
    if os.path.exists(json_path):
        commands = json.loads(open(json_path, 'r').read())
    fields = {'desc': desc, 'alias': alias}
    commands[cmd] = fields
    with open(json_path, 'w') as f:
        f.write(json.dumps(commands))


def read_commands():
    json_path = os.path.join(dir_path, 'commands.json')
    if not os.path.exists(json_path):
        return None
    commands = json.loads(open(json_path, 'r').read())
    return commands


def write_commands(commands):
    json_path = os.path.join(dir_path, 'commands.json')
    with open(json_path, 'w') as f:
        f.write(json.dumps(commands))


def grep_commands(pattern):
    commands = read_commands()
    result = None
    if commands:
        result = []
        for cmd, fields in commands.items():
            desc = fields['desc']
            alias = fields['alias']
            if alias == pattern and alias.strip() != "":
                result.clear()
                result.append((cmd, desc))
                break
            if re.search(pattern, cmd + " :: " + desc):
                result.append((cmd, desc))
                continue
            # Show if all the parts of the pattern are in one command/desc
            keywords_len = len(pattern.split())
            i_keyword = 0
            for keyword in pattern.split():
                if keyword.lower() in cmd.lower() or keyword.lower() in desc.lower():
                    i_keyword += 1
            if i_keyword == keywords_len:
                result.append((cmd, desc))
    return result


def select_command(commands):
    click.echo("", err=True)
    for idx, command in enumerate(commands):
        cmd, desc = command
        click.secho(f" {idx + 1} \t", nl=False, fg='yellow', err=True)
        click.secho(f" {cmd} :: {desc}", fg='green', err=True)

    selection = 1
    while True and len(commands) > 1:
        click.echo("", err=True)
        selection = click.prompt(
            f"Select a command [1-{len(commands)}] (0 to cancel)",
            type=int,
            err=True
        )
        if selection in range(len(commands) + 1):
            break
        click.echo("Number is not in range", err=True)
    return selection - 1


def edit_commands(commands, editor=None, edit_header=""):
    edit_msg = [edit_header]
    for cmd, fields in commands.items():
        desc, alias = fields['desc'], fields['alias']
        cmd = json.dumps(cmd)
        desc = json.dumps(desc)
        alias = json.dumps(alias)
        edit_msg.append("{} :: {} :: {}".format(cmd, alias, desc))
    edited = click.edit('\n'.join(edit_msg), editor=editor)

    command_regex = re.compile(r'(\".*\")\s*::\s*(\".*\")\s*::\s*(\".*\")')
    new_commands = {}
    if edited:
        for line in edited.split('\n'):
            if (line.startswith('#') or line == ""):
                continue
            re_match = command_regex.search(line)
            if re_match and len(re_match.groups()) == 3:
                cmd, alias, desc = re_match.groups()
                try:
                    cmd = json.loads(cmd)
                    desc = json.loads(desc)
                    alias = json.loads(alias)
                except ValueError:
                    click.echo("Error parsing json from edit file.")
                    return None
                new_commands[cmd] = {'desc': desc, 'alias': alias}
            else:
                click.echo("Could not read line '{}'".format(line))
    return new_commands


def format_commands(commands):
    res = []
    for cmd, fields in commands.items():
        desc, alias = fields['desc'], fields['alias']
        res.append("$ {} :: {} :: {}".format(cmd, alias, desc))
    return res


def create_pcmd(command):
    class KeepCommandTemplate(string.Template):
        default_sep = '='
        idpattern = r'[_a-z][_a-z0-9{}]*'.format(default_sep)

        def __init__(self, template):
            super().__init__(template)
    return KeepCommandTemplate(command)


def get_params_in_pcmd(pcmd):
    patt = pcmd.pattern
    params = []
    defaults = []
    raw = []
    for match in re.findall(patt, pcmd.template):
        var = match[1] or match[2]
        svar = var.split(pcmd.default_sep)
        p, d = svar[0], pcmd.default_sep.join(svar[1:])
        if p and p not in params:
            raw.append(var)
            params.append(p)
            defaults.append(d)
    return raw, params, defaults


def substitute_pcmd(pcmd, kargs, safe=False):
    if safe:
        return pcmd.safe_substitute(**kargs)
    else:
        return pcmd.substitute(**kargs)


def get_github_token():
    token_file_path = os.path.join(dir_path, '.credentials')
    token = None

    if os.path.exists(token_file_path):
        with open(token_file_path) as token_file:
            token = json.load(token_file)

    if not token or 'token' not in token or not token['token']:
        click.secho('Github access token not found :(', fg='red')
        click.secho('Use the "keep github_token" command to store the token first', fg='red')
        return None

    return token
