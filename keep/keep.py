import sys
import os


HOME = os.path.expanduser('~')
KEEP_FILE = HOME + '/.keep'  # File to store commands
KEEPN_FILE = HOME + '/.keep_info'  # File to store number of commands


def print_error_message():
    print("Usages :\n1. keep [options]")
    print("Options: list | reset ")
    print("2. keep <command_name> \n <brief_description_of_the_command>")
    print("3. keep grep <search terms in the description>")


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
            print(str(cmdno) + "." + line[:], end="")

        f.close()
    elif command[0] == 'reset':
        prompt = input("This will erase all of your stored commands. "
                       "Proceed ? (y/N)")
        if prompt.strip() in ('y', 'Y'):
            try:
                os.remove(KEEP_FILE)
            except FileNotFoundError:
                pass
            try:
                os.remove(KEEPN_FILE)
            except FileNotFoundError:
                pass
        else:
            print("Aborted.")
    elif command[0] == 'grep':
        sstring = sys.argv[2:]
        sstring = ' '.join(sstring)
        if not sstring:
            print("No search terms")
            sys.exit()
        try:
            f = open(KEEP_FILE, 'r')
            i = 0
            for line in f.readlines():
                s = (line.split(":")[1]).strip()
                if not s.find(sstring.strip()) == -1:
                    print(line)
                    i += 1
            if i == 0:
                print("No matched terms")
            f.close()
        except IOError:
            print("You have no saved commands")
    else:
        if not os.path.exists(KEEPN_FILE):
            f = open(KEEPN_FILE, 'w')
            f.write('0\n')
            f.close()
        new = ' '.join(command)
        try:
            f = open(KEEP_FILE, 'r')
            for line in f.readlines():
                if new.strip() == (line.split(":")[0])[2:].strip():
                    print("Command already present")
                    print(line)
                    f.close()
                    sys.exit()
            f.close()
        except IOError:
            pass
        f = open(KEEP_FILE, 'a')
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
