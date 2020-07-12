from shlex import quote

import click
from keep import cli, utils


@click.command('completion', short_help='Command completion helper.')
@click.option('--bash', 'shell', flag_value='bash', default=True)
@click.option('--zsh', 'shell', flag_value='zsh')
@cli.pass_context
def cli(ctx, shell):
    """Completion helpers for keep"""
    commands = utils.read_commands()

    if shell == 'zsh':
        for cmd, fields in commands.items():
            print("{cmd}:{desc}".format(cmd=cmd, desc=fields['desc']))
    elif shell == 'bash':
        for cmd in commands.keys():
            print(quote(cmd))
