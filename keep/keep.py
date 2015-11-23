from __future__ import print_function
import getpass
import sys

def main():
    command = sys.argv[1:]

    if command[0] in ['show', 'list']:
        f = open("/home/" + getpass.getuser() + "/.keep", 'r')
        for line in f.readlines():
            print(line)
        f.close()
    else:
        f = open("/home/" + getpass.getuser() + "/.keep", 'a')
        new = ' '.join(command)
        desc = sys.stdin.readline()
        f.write('$ ' + new + '\n')
        f.write(desc)
        f.close()

