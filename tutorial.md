# Tutorial

- Initialize Keep with `keep init`. This creates a `.keep` directory in your home folder.
- Start saving commands using `keep new`.
- Once you have saved couple of commands, start using `keep grep`.
-- This is not exactly similar to `keep list | grep` as `keep grep` search is more powerful.
- Have fun !

# Commands

<dl>
  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_update.py">edit</a></dt>
  <dd>Edit the saved commands and their descriptions.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_grep.py">grep</a> "PATTERN"</dt>
  <dd>This is used to search for saved commands.<br><br>Argument passed to <code>keep grep</code> is interpreted in two ways. First, it is interpreted as a regular expression and if it matches any command or description, then the search is displayed. If this fails, the argument is then splitted and the individule words of the argument are searched in the commands and the descriptions. If all the splits of the argument are found in a command or a discription, the result is displayed.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_init.py">init</a></dt>
  <dd>Initializes the CLI.<br><br>The CLI is supposed to be installed if there exists a <code>.keep</code> direcotry in the home directory. Once installed, this command is not supposed if the user intends to reset the local database of keep.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_list.py">list</a></dt>
  <dd>Shows the saved commands.<br><br>Keep uses tabulate library to show the result. If the command length is long, the table may look like in need of wrapping. But increasing the terminal width works for the best.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_new.py">new</a></dt>
  <dd>Saves new command locally.<br><br>If the command already exists, it updates the previously stored description.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_rm.py">rm</a></dt>
  <dd>Deletes a command.<br><br>Input the exact command you have saved and this removes it from the local storage. 

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_run.py">run</a> "PATTERN".</dt>
  <dd>Executes a saved command.<br><br>Pattern works in the same way as in <code>keep grep</code></dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_update.py">update</a></dt>
  <dd>Checks for an update on pypi.</dd>

</dl>
