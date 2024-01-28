##
## MyChess
## main
## File description:
## main
##

from sys import argv, exit
from src.utils import args_manager
from src.user import User

if __name__ == '__main__':
    username, year, month = args_manager(argv[1:])
    user = User(username, year, month)

    if year and month:
        user.getPgn()
    else:
        user.getData()
    exit(0)