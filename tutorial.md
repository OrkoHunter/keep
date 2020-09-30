# Tutorial

 - Initialize Keep with `keep init`. This creates a `.keep` directory in your home folder.
 - Start saving commands using `keep new`.
 - Once you have saved couple of commands, start using `keep grep`.
  - This is not exactly similar to `keep list | grep` as `keep grep` search is more powerful.
 - Use `keep github_token` to register a GitHub token for gist as backup. It is then stored inside your `~/.keep/.credentials` file.
 - Now it's time to store the commands on github gists. Use `keep push`.
  - **NOTE: keep creates a secret GitHub gist. They can still be accessed using the direct URL of the gist.**
 - If you have got another computer, install `keep` on it. Do `keep init`. Copy your `~/.keep/.credentials` over to that computer in the same location, or follow `keep github_token`.
 - Do `keep pull` to retrieve all the saved commands.
 - Have fun !

# Commands

<dl>
  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_update.py">edit</a></dt>
  <dd>Edit the saved commands and their descriptions.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_grep.py">grep</a> "PATTERN"</dt>
  <dd>This is used to search for saved commands.<br><br>Argument passed to <code>keep grep</code> is interpreted in two ways. First, it is interpreted as a regular expression and if it matches any command or description, then the search is displayed. If this fails, the argument is then splitted and the individule words of the argument are searched in the commands and the descriptions. If all the splits of the argument are found in a command or a discription, the result is displayed.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_init.py">init</a></dt>
  <dd>Initializes the CLI.<br><br>The CLI is supposed to be installed if there exists a <code>.keep</code> direcotry in the home directory. Once installed, this command is not supposed to be used unless the user intends to reset the local database of keep.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_list.py">list</a></dt>
  <dd>Shows the saved commands.<br><br>Keep uses tabulate library to show the result. If the command length is long, the table may look like in need of wrapping. But increasing the terminal width works for the best.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_new.py">new</a></dt>
  <dd>Saves new command locally.<br><br>If the command already exists, it updates the previously stored description.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_pull.py">pull</a></dt>
  <dd>Updates the local commands with saved GitHub gist.<br><br>Once registered, this command fetches your database saved on the remote (GitHub gist) and updates the local storage.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_push.py">push</a></dt>
  <dd>Updates GitHub gist with local commands.<br><br>This command updates the remote (GitHub gist) with the local storage. Consider using this command before storing a new command on some other computer without pulling the latest changes.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_github_token.py">github_token</a></dt>
  <dd>Register a GitHub token.<br><br>Register a GitHub token to use push and pull commands with a GitHub gist.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_rm.py">rm</a></dt>
  <dd>Deletes a command.<br><br>Input the exact command you have saved and this removes it from the local storage. If the user uses <code>push</code> after removing any command, the same will be overwritten on the remote.</dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_run.py">run</a> "PATTERN".</dt>
  <dd>Executes a saved command.<br><br>Pattern works in the same way as in <code>keep grep</code></dd>

  <dt><a href="https://github.com/OrkoHunter/keep/blob/master/keep/commands/cmd_update.py">update</a></dt>
  <dd>Checks for an update on pypi.</dd>

</dl>

# Pro Tip - Commands with parameters

When saving a new command with `keep new`, if a word is prefixed with `$` while saving a command with Keep, it is treated as a variable and Keep asks for an input.

_Examples:_

- Adding parameters through Keep input
```bash
$ keep run "tar"

 1	$ tar zxvf $tarfile -C $dest :: Extract tar content to destination

Enter value for 'tarfile': /path/to/tar
Enter value for 'dest': /my/folder/

Execute
	$ tar zxvf /path/to/tar -C /my/folder/ :: Extract tar content to destination
? [Y/n]:
```

- Parameters can also be passed directly into commands.

```bash
$ keep run "grep" /path/to/dir "data[0-9]+" "> file"

 1	$ grep -irnw $dir -e $pattern $out :: Look for a regex pattern inside files

dir: /path/to/dir
pattern: data[0-9]+
out: > file

Execute
	$ grep -irnw /path/to/dir -e file_[0-9]+ > file :: Look for a regex pattern inside files
? [Y/n]:
```

- If any required parameter is missed out, Keep will ask its input separately.

```bash
$ keep run "grep" /path/to/dir "data[0-9]+"

 1	$ grep -irnw $dir -e $pattern $out :: Look for a regex pattern inside files

dir: /path/to/dir
pattern: data[0-9]+
Enter value for 'out':

Execute
	$ grep -irnw /path/to/dir -e data[0-9]+   :: Look for a regex pattern inside files
? [Y/n]:
```

- Disable confirm message before run
```bash
$ keep run "tar" -n

 1  $ tar zxvf $tarfile -C $dest :: Extract tar content to destination

Enter value for 'tarfile': /path/to/tar
Enter value for 'dest': /my/folder/

```