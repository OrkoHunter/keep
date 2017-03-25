import os
import click
from keep import cli, utils


@click.command('run', short_help='Executes a saved command.',
               context_settings=dict(ignore_unknown_options=True))
@click.argument('pattern')
@click.argument('arguments', nargs=-1, type=click.UNPROCESSED)
@click.option('--safe', is_flag=True, help='Ignore missing arguments')
@cli.pass_context
def cli(ctx, pattern, arguments, safe):
    """Executes a saved command."""

    matches = utils.grep_commands(pattern)
    if matches:
        click.echo("\n\n")
        for idx, match in enumerate(matches):
            cmd, desc = match
            click.secho(" " + str(idx + 1) + "\t", nl=False, fg='yellow')
            click.secho("$ {} :: {}".format(cmd, desc), fg='green')
        click.echo("\n\n")

        selection = 1
        while True and len(matches) > 1:
            selection = click.prompt("Choose command to execute [1-{}] (0 to cancel)"
                                     .format(len(matches)), type=int)
            if selection in range(len(matches) + 1):
                break
            click.echo("Number is not in range")
        if selection > 0:
            cmd, desc = matches[selection - 1]
            pcmd = utils.create_pcmd(cmd)
            params = utils.get_params_in_pcmd(pcmd)

            arguments = list(arguments)
            kargs = {}
            for p in params:
                if arguments:
                    val = arguments.pop(0)
                    click.echo("{}: {}".format(p, val))
                    kargs[p] = val
                elif not safe:
                    val = click.prompt("Enter value for '{}'".format(p))
                    kargs[p] = val
            click.echo("\n")

            final_cmd = utils.substitute_pcmd(pcmd, kargs, safe)

            command = "$ {} :: {}".format(final_cmd, desc)
            if click.confirm("Execute\n\t{}\n\n?".format(command), default=True):
                os.system(final_cmd)
    elif matches == []:
        click.echo('No saved commands matches the pattern {}'.format(pattern))
    else:
        click.echo("No commands to run, Add one by 'keep new'. ")
