# Tutorial

 - Initialize Keep with `keep init`. This creates a `.keep` directory in your home folder.
 - You are then asked to register.
  - It asks for your Email because that is unique to you. It is just another username and thus you can input anything
     unique to you.
  - You can choose to not register this time and later start the process by using `keep register`.
  - You can use Keep CLI without registering if you do not intend to use the server for storing or fetching your commands.
 - It generates a 255 bit password for you. It is then stored inside your `~/.keep/.credentials` file.
 - Start saving commands using `keep new`.
 - Once you have saved couple of commands, start using `keep grep`.
  - This is not exactly similar to `keep list | grep` as `keep grep` search is more powerful.
 - Now it's time to store the commands on the server. Use `keep push`.
 - If you have got another computer, install `keep` on it. Do `keep init` and skip registration. Copy your `~/.keep/.credentials` over to that computer in the same location.
 - Do `keep pull` to retrieve all the saved commands.
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

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_pull.py">pull</a></dt>
  <dd>Updates the local commands with remote.<br><br>Once registered, this command fetches your database saved on the remote and updates the local storage.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_push.py">push</a></dt>
  <dd>Updates remote with local commands.<br><br>This command updates the remote database with the local storage. Consider using this command before storing a new command on some other computer without pulling the latest changes.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_register.py">register</a></dt>
  <dd>Create remote for the user.<br><br>If not registered while <code>keep init</code>, this command can be used for the same purpose in future.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_rm.py">rm</a></dt>
  <dd>Deletes a command.<br><br>Input the exact command you have saved and this removes it from the local storage. If the user uses <code>push</code> after removing any command, the same will be overwritten on the remote.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_run.py">run</a> "PATTERN".</dt>
  <dd>Executes a saved command.<br><br>Pattern works in the same way as in <code>keep grep</code></dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_update.py">update</a></dt>
  <dd>Checks for an update on pypi.</dd>

</dl>
