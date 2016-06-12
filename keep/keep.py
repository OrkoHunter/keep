import sys
import os

HOME = os.path.expanduser('~')

def print_error_message():
    print("Usages :\n1. keep [options]")
    print("Options: show | list ")
    print("2. keep <command_name> \n <brief_description_of_the_command>")

def main():
    command = sys.argv[1:]
    if not command:
        print_error_message()
        sys.exit(2)
    if command[0] == 'show':
        try:
            f = open(HOME + "/.keep", 'r')
        except IOError:
            print("You have no saved commands")
            sys.exit(2)
        lineno = cmdno = 0
        for line in f.readlines():
            lineno += 1
            if lineno % 2 != 0:
                cmdno += 1
                sys.stdout.write("-"*50 + "\n")
                sys.stdout.write(str(cmdno) + ". " + line[2:])
            else:
                sys.stdout.write(line)
        f.close()
    elif command[0] == 'list':
        try:
            f = open(HOME + "/.keep", 'r')
        except IOError:
            print("You have no saved commands.")
            sys.exit(2)
        cmdno = 0
        for line in f.readlines():
            if (line[0]=='$'):
                cmdno += 1
                print(str(cmdno) + ". " + line[2:], end="")
        f.close()
    else:
        f = open(HOME + "/.keep", 'a')
        new = ' '.join(command)
        desc = sys.stdin.readline("Description : ")
        f.write('$ ' + new + '\n')
        f.write(desc)
        f.close()


"""
    Structure of the file ~/.keep
    -----------------------------

    First line, first word contains the number of commands already stored.
    Next lines
"""

