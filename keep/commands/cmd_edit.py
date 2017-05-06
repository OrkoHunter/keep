import click
from keep import cli, utils


@click.command('edit', short_help='Edit a saved command.')
@click.option('--editor', help='Editor to use')
@cli.pass_context
def cli(ctx, editor):
    """Edit saved commands."""

    commands = utils.read_commands()
    if commands is []:
        click.echo("No commands to edit, Add one by 'keep new'. ")
    else:
        edit_header = "# Unchanged file will abort the operation\n"
        new_commands = utils.edit_commands(commands, editor, edit_header)
        if new_commands and new_commands != commands:
            click.echo("Replace:\n")
            click.secho("\t{}".format('\n\t'.join(utils.format_commands(commands))),
                        fg="green")
            click.echo("With:\n\t")
            click.secho("\t{}".format('\n\t'.join(utils.format_commands(new_commands))),
                        fg="green")
            if click.confirm("", default=False):
                utils.write_commands(new_commands)
