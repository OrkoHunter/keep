import click
from keep import cli, utils, about

@click.command('update', short_help='Check for an update of Keep.')
@cli.pass_context
def cli(ctx):
    """Check for an update of Keep."""
    utils.check_update(ctx, forced=True)
    click.secho("Keep is at its latest version v{}".format(about.__version__), fg='green')
