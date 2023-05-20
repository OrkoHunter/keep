import click
from keep import cli, utils

@click.command("new", short_help="Saves a new command.")
@click.option("--cmd", help="The command to save")
@click.option("--desc", help="The description of the command")
@click.option("--alias", default="", help="The alias of the command")
@cli.pass_context
def cli(ctx, cmd, desc, alias):
    """Saves a new command"""
    if not cmd:
        cmd = click.prompt("Command")
    if not desc:
        desc = click.prompt("Description")
    if not alias:
        alias = click.prompt("Alias (optional)", default="")
    utils.save_command(cmd, desc, alias)

    utils.log(ctx, "Saved the new command - {} - with the description - {}.".format(cmd, desc))
