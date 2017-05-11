import click
from keep import cli, utils


@click.command('rm', short_help='Deletes a saved command.')
@click.argument('pattern')
@cli.pass_context
def cli(ctx, pattern):
    """Deletes a saved command."""
    matches = utils.grep_commands(pattern)
    if matches:
        selected = utils.select_command(matches)
        if selected >= 0:
            cmd, desc = matches[selected]
            command = "$ {} :: {}".format(cmd, desc)
            if click.confirm("Remove\n\t{}\n\n?".format(command), default=True):
                utils.remove_command(cmd)
                click.echo('Command successfully removed!')
    elif matches == []:
        click.echo('No saved commands matches the pattern {}'.format(pattern))
    else:
        click.echo("No commands to remove, Add one by 'keep new'. ")
