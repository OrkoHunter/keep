#/usr/bin/env bash

function _keep()
{
  local cur prev commands
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"
  commands="edit github_token grep init list new pull push rm run update"

  case "$prev" in
    run|rm)
      mapfile -t COMPREPLY < <(compgen -W "$(keep completion --bash)" -- $cur)
      ;;
    edit)
      COMPREPLY=("--editor")
      ;;
    keep)
      COMPREPLY=( $(compgen -W "-h -v --verbose $commands" -- $cur) )
      ;;
  esac

  return 0

}

complete -F _keep keep
