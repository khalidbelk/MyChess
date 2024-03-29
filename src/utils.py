##
## MyChess
## utils
## File description:
## utils
##

def parse_data(data):
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

def usage():
    print('USAGE: ./mychess -u user [gamesYear gamesMonth]')
    print('\tuser\t\tis the Chess.com username. This flag alone provides information about the user.')
    print("\tgamesYear\tis the year of the user's games you want to download")
    print("\tgamesMonth\tis the month of the user's games you want to download")

def args_manager(args: list[str]):
    username = ''
    year = None
    month = None

    try:
        for i in range (len(args)):
            arg = args[i]
            if arg == '-help':
                usage()
                exit(0)
            if arg == '-u':
                username = args[i + 1]
                if i + 3 < len(args):
                    year = args[i + 2]
                    month = args[i + 3]
    except IndexError:
        print('Error: Missing argument(s). Use -help for more information.')
        exit(84)

    if username == '':
        print('Username mising, please insert an username.')
        exit(84)

    return username, year, month