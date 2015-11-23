from __future__ import print_function
import getpass
import sys

def main():
    command = sys.argv[1:]

    if command[0] == 'show':
        try:
            f = open("/home/" + getpass.getuser() + "/.keep", 'r')
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
            f = open("/home/" + getpass.getuser() + "/.keep", 'r')
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
        f = open("/home/" + getpass.getuser() + "/.keep", 'a')
        new = ' '.join(command)
        desc = sys.stdin.readline()
        f.write('$ ' + new + '\n')
        f.write(desc)
        f.close()

