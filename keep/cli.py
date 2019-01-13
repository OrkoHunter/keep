import os
import sys
import click

from keep import utils

CONTEXT_SETTINGS = dict(auto_envvar_prefix='KEEP')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


# Directory containing the commands modules
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))
pass_context = click.make_pass_decorator(Context, ensure=True)


class KeepCLI(click.MultiCommand):

    def pre_process(self, ctx):
        dir_path = os.path.join(os.path.expanduser('~'), '.keep')
        if not os.path.exists(dir_path):
            utils.first_time_use(ctx)
        else:
            utils.check_update(ctx)

    def list_commands(self, ctx):
        self.pre_process(ctx)
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        self.pre_process(ctx)
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('keep.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=KeepCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose):
    """
    Keep and view shell commands in terminal only.

    Read more at https://github.com/orkohunter/keep
    """
    ctx.verbose = verbose
