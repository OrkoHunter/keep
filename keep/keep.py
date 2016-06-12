import sys
import os

HOME = os.path.expanduser('~')
KEEP_FILE = HOME + '/.keep'  # File to store commands
KEEPN_FILE = HOME + '/.keep_info'  # File to store number of commands


def print_error_message():
    print("Usages :\n1. keep [options]")
    print("Options: show | list ")
    print("2. keep <command_name> \n <brief_description_of_the_command>")

def main():
    command = sys.argv[1:]
    if not command:
        print_error_message()
        sys.exit(2)
    elif command[0] == 'list':
        try:
            f = open(KEEP_FILE, 'r')
        except IOError:
            print("You have no saved commands.")
            sys.exit(2)
        cmdno = 0
        for line in f.readlines():
            cmdno += 1
            print(str(cmdno) + "." + line[1:], end="")
        f.close()
    elif command[0] == 'reset':
        try:
            os.remove(KEEP_FILE)
        except FileNotFoundError:
            pass
        try:
            os.remove(KEEPN_FILE)
        except FileNotFoundError:
            pass
    else:
        if not os.path.exists(KEEPN_FILE):
            f = open(KEEPN_FILE, 'w')
            f.write('0\n')
            f.close()

        f = open(KEEP_FILE, 'a')
        new = ' '.join(command)
        desc = input("Description : ")
        f.write('$ ' + new + ' : ')
        f.write(desc + '\n')
        f.close()

        f = open(KEEPN_FILE, 'r')
        n = int(f.readline())
        f.close()
        f = open(KEEPN_FILE, 'w')
        f.write(str(n+1) + '\n')
        f.close()


"""
    Structure of the file ~/.keep
    -----------------------------

    $ + Command + : + Description

    Structure of the file ~/.keep_info
    ----------------------------------

    Total count of commands saved
"""

