##
## MyChess
## main
## File description:
## main
##

from sys import argv, exit
from src.user import User

def usage():
    print('USAGE: ./mychess -u user -help')
    print('\tuser\tis the Chess.com username')

def args_manager(args: list[str]):
    username = ''

    try:
        for i in range (len(args)):
            arg = args[i]
            if arg == '-help':
                usage()
                exit(0)
            if arg == '-u':
                username = args[i + 1]
    except IndexError:
        print('Error: Missing argument(s). Use -help for more information.')
        exit(84)

    if username == '':
        print('Username mising, please insert an username.')
        exit(84)

    return username

if __name__ == '__main__':
    username = args_manager(argv[1:])

    user = User(username)
    user.getData()
    exit(0)