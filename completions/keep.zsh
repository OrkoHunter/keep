#compdef _keep keep

function _keep {
  local -a commands

  _arguments -C \
    "-v[Enables verbose mode]:" \
    "--verbose[Enables verbose mode]:" \
    "--help[Show the help message and exit]:" \
    "1: :->cmnds" \
    "*::arg:->args"
  case $state in
  cmnds)
    commands=(
      "edit:Edit a saved command."
      "github_token:Register a GitHub Token to use GitHub Gists as a backup."
      "grep:Searches for a saved command."
      "init:Initializes the CLI."
      "list:Shows the saved commands."
      "new:Saves a new command."
      "pull:Pull commands from saved GitHub gist."
      "push:Push commands to a secret GitHub gist."
      "rm:Deletes a saved command."
      "run:Executes a saved command."
      "update:Check for an update of Keep."
    )
    _describe "command" commands
    ;;
  esac

  case "$words[1]" in
  edit)
    _keep_edit
    ;;
  rm)
    _keep_commands
    ;;
  run)
    _keep_commands
    ;;
  esac
}

function _keep_edit {
  _arguments \
    "--editor[Editor to use]"
}

function _keep_commands {
  local -a commands
  commands=("${(@f)$(keep completion --zsh)}")
  _describe "command" commands
}
