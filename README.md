![logo](https://raw.githubusercontent.com/OrkoHunter/keep/master/data/logo.png#gh-light-mode-only)

![logo](./data/logo-white.png#gh-dark-mode-only)

[![PyPI](https://img.shields.io/pypi/v/keep)](https://github.com/orkohunter/keep/releases) ![PyPI - Downloads](https://img.shields.io/pypi/dm/keep)

# A Meta CLI toolkit

> Your personal shell command keeper

## Why?

Writwick Wraj loves using the command line.

Writwick googles \"How to do X in terminal?\" and multiple forums and
blog posts finally provide him the magical _command_ for the rescue.
Problem Solved !

Fast forward couple weeks, Writwick has to do X in terminal, again. Wraj
remembers solving this few weeks ago. Let him do a reverse-i-search with
_Ctrl+R_. Nope, can\'t remember sh\*t. Browser search history? 25 web
pages found matching _X_. Argh!

Writwik finally finds the solution. From this time Writwik starts
writing the commands somewhere online for the future.

Wait, why shouldn\'t he keep the command in his terminal itself if this
is only place where he\'ll ever have use it?

## Features

- Save a new command with a brief description
- Search the saved commands using powerful patterns
- Save the commands as a secret GitHub gist
- Use `keep push` and `keep pull` to sync the commands between GitHub
  gist and other computers.

**ProTip : Save the commands you usually forget in ssh sessions and sync
it with your local machine.**

## Installation

    $ pip3 install keep

Use Python 3.6 or later.

You can install pip3 using apt-get as `sudo apt install python3-pip`.

## Usage

    Usage: keep [OPTIONS] COMMAND [ARGS]...

      Keep and view shell commands in terminal only.

      Read more at https://github.com/orkohunter/keep

    Options:
      -v, --verbose  Enables verbose mode.
      --help         Show this message and exit.

    Commands:
      edit          Edit a saved command.
      github_token  Register a GitHub Token to use GitHub Gists as a backup.
      grep          Searches for a saved command.
      init          Initializes the CLI.
      list          Shows the saved commands.
      new           Saves a new command.
      pull          Pull commands from saved GitHub gist.
      push          Push commands to a secret GitHub gist.
      rm            Deletes a saved command.
      run           Executes a saved command.
      update        Check for an update of Keep.

[See the detailed usage and
tutorial.](https://github.com/OrkoHunter/keep/blob/master/tutorial.md)

### Command-line Completion

To enable command-line completion (TAB completion) follow these steps for the shell of your choice

#### bash

1. Create a directory in your home directory called `.bash`

        mkdir -p $HOME/.bash

2. Copy [completion/keep.bash](https://github.com/OrkoHunter/keep/blob/master/completions/keep.bash) to `$HOME/.bash/keep`

        curl -SLo "$HOME/.bash/keep" "https://raw.githubusercontent.com/OrkoHunter/keep/master/completions/keep.bash"

3. Add the following lines to `$HOME/.bashrc` file

        [ -f "$HOME/.bash/keep" ] && . "$HOME/.bash/keep"

#### zsh

1. Create a directory in your home called `.zsh`

        mkdir -p $HOME/.zsh

2. Copy [completion/keep.zsh](https://github.com/OrkoHunter/keep/blob/master/completions/keep.zsh) to `$HOME/.zsh/_keep`

        curl -SLo "$HOME/.zsh/_keep" "https://raw.githubusercontent.com/OrkoHunter/keep/master/completions/keep.zsh"

3. Add the following lines inside `$HOME/.zshrc` file

        fpath=($HOME/.zsh $fpath)
        autoload -Uz compinit && compinit

### Contribute

This is a very young project. If you have got any suggestions for new
features or improvements, please comment over
[here](https://github.com/OrkoHunter/keep/issues/11). Pull Requests are
most welcome !

❤

---

Not a command line fanatic? Here are some resources for you :

- <https://github.com/jlevy/the-art-of-command-line>
- <https://github.com/herrbischoff/awesome-osx-command-line>
- <https://github.com/alebcay/awesome-shell>
- <https://github.com/aharris88/awesome-cli-apps>
