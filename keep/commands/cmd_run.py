import os
import click
from keep import cli, utils


@click.command('run', short_help='Executes a saved command.')
@click.argument('pattern')
@cli.pass_context
def cli(ctx, pattern):
    """Executes a saved command."""
    matches = utils.grep_commands(pattern)
    if matches:
        click.echo("\n\n")
        for idx, match in enumerate(matches):
            cmd, desc = match
            click.secho(" " + str(idx + 1) + "\t", nl=False, fg='yellow')
            click.secho("$ {} :: {}".format(cmd, desc), fg='green')
        click.echo("\n\n")

        val = 1
        while True and len(matches) > 1:
            val = click.prompt("Choose command to execute [1-{}] (0 to cancel)"
                               .format(len(matches)), type=int)
            if val in range(len(matches) + 1):
                break
            click.echo("Number is not in range")
        if val > 0:
            cmd, desc = matches[val - 1]
            command = "$ {} :: {}".format(cmd, desc)
            if click.confirm("Execute\n\t{}\n\n?".format(command), default=True):
                os.system(cmd)
    elif matches == []:
        click.echo('No saved commands matches the pattern {}'.format(pattern))
    else:
        click.echo("No commands to run, Add one by 'keep new'. ")
