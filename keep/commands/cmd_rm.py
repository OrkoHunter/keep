import click
from keep import cli, utils


@click.command('rm', short_help='Deletes a saved command.')
@click.argument('pattern')
@cli.pass_context
def cli(ctx, pattern):
    """Deletes a saved command."""
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
            val = click.prompt("Choose command to remove [1-{}] (0 to cancel)"
                               .format(len(matches)), type=int)
            if val in range(len(matches) + 1):
                break
            click.echo("Number is not in range")
        if val > 0:
            cmd, desc = matches[val - 1]
            command = "$ {} :: {}".format(cmd, desc)
            if click.confirm("Remove\n\t{}\n\n?".format(command), default=True):
                commands = utils.read_commands()
                del commands[cmd]
                utils.write_commands(commands)
                click.echo('Command successfully removed!')
    elif matches == []:
        click.echo('No saved commands matches the pattern {}'.format(pattern))
    else:
        click.echo("No commands to remove, Add one by 'keep new'. ")
