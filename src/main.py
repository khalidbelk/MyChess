##
## MyChess
## main
## File description:
## main
##

from sys import argv, exit

def usage():
    print('USAGE: ./mychess -u user -help')
    print('\tuser\tis the Chess.com username')

def args_manager(args: list[str]):
    user = ''
    try:
        for i in range (len(args)):
            arg = args[i]
            if arg == '-help':
                usage()
                exit(0)
            if arg == '-u':
                user = args[i + 1]
    except IndexError:
        print('Error: Missing argument(s). Use -help for more information.')
        exit(84)

    if user == '':
        print('Username mising, please insert an username.')
        exit(84)

    return user

if __name__ == '__main__':
    user = args_manager(argv[1:])
    print(user)
    exit(0)