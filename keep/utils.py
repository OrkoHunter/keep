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
import tabulate

from keep import about

# Directory for Keep files
dir_path = os.path.join(os.path.expanduser('~'), '.keep')


def check_update(forced=False):
    update_check_file = os.path.join(dir_path, 'update_check.json')
    today = datetime.date.today().strftime("%m/%d/%Y")
    if os.path.exists(update_check_file):
        dates = json.loads(open(update_check_file, 'r').read())
    else:
        dates = []
    if today not in dates or forced:
        dates.append(today)
        if os.path.exists(update_check_file):
            with open(update_check_file, 'w') as f:
                f.write(json.dumps(dates))
        r = requests.get("https://pypi.python.org/pypi/keep/json").json()
        version = r['info']['version']
        curr_version = about.__version__
        if version != curr_version:
            click.secho("Keep seems to be outdated. Current version = "
                        "{}, Latest version = {}".format(curr_version, version) +
                        "\n\nPlease update with ", bold=True, fg='red')
            click.secho("\tpip --no-cache-dir install -U keep==" + str(version), fg='green')
            sys.exit(0)


def first_time_use(ctx):
    click.secho("Initializing environment in ~/.keep directory", fg='green')
    for i in range(2):
        click.echo('.', nl=False)
        time.sleep(0.5)
    click.echo('.OK', nl=True)

    os.mkdir(dir_path)

    sys.exit(0)


def list_commands(ctx):
    commands = read_commands()
    table = []
    for cmd, desc in commands.items():
        table.append(['$ ' + cmd, desc])
    print(tabulate.tabulate(table, headers=['Command', 'Description']))


def log(ctx, message):
    """Prints log when verbose set to True."""
    if ctx.verbose:
        ctx.log(message)


def remove_command(cmd):
    commands = read_commands()
    if cmd in commands:
        del commands[cmd]
        write_commands(commands)
    else:
        click.echo('Command - {} - does not exist.'.format(cmd))


def save_command(cmd, desc):
    json_path = os.path.join(dir_path, 'commands.json')
    commands = {}
    if os.path.exists(json_path):
        commands = json.loads(open(json_path, 'r').read())
    commands[cmd] = desc
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
        for cmd, desc in commands.items():
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
    click.echo("\n\n")
    for idx, command in enumerate(commands):
        cmd, desc = command
        click.secho(" " + str(idx + 1) + "\t", nl=False, fg='yellow')
        click.secho("$ {} :: {}".format(cmd, desc), fg='green')
    click.echo("\n\n")

    selection = 1
    while True and len(commands) > 1:
        selection = click.prompt(
            "Select a command [1-{}] (0 to cancel)"
            .format(len(commands)), type=int)
        if selection in range(len(commands) + 1):
            break
        click.echo("Number is not in range")
    return selection - 1


def edit_commands(commands, editor=None, edit_header=""):
    edit_msg = [edit_header]
    for cmd, desc in commands.items():
        cmd = json.dumps(cmd)
        desc = json.dumps(desc)
        edit_msg.append("{} :: {}".format(cmd, desc))
    edited = click.edit('\n'.join(edit_msg), editor=editor)

    command_regex = re.compile(r'(\".*\")\s*::\s*(\".*\")')
    new_commands = {}
    if edited:
        for line in edited.split('\n'):
            if (line.startswith('#') or line == ""):
                continue
            re_match = command_regex.search(line)
            if re_match and len(re_match.groups()) == 2:
                cmd, desc = re_match.groups()
                try:
                    cmd = json.loads(cmd)
                    desc = json.loads(desc)
                except ValueError:
                    click.echo("Error parsing json from edit file.")
                    return None
                new_commands[cmd] = desc
            else:
                click.echo("Could not read line '{}'".format(line))
    return new_commands


def format_commands(commands):
    res = []
    for cmd, desc in commands.items():
        res.append("$ {} :: {}".format(cmd, desc))
    return res


def create_pcmd(command):
    return string.Template(command)


def get_params_in_pcmd(pcmd):
    patt = pcmd.pattern
    res = []
    for match in re.findall(patt, pcmd.template):
        param = match[1] or match[2]
        if param and param not in res:
            res.append(param)
    return res


def substitute_pcmd(pcmd, kargs, safe=False):
    if safe:
        return pcmd.safe_substitute(**kargs)
    else:
        return pcmd.substitute(**kargs)
