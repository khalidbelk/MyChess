##
## MyChess
## user
## File description:
## user
##

import requests
from src.utils import parse_data

baseUrl = "https://api.chess.com/pub/player/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

class User:
    def __init__(self, username: str):
        self.username = username

    def getData(self):
        try:
            url = f"{baseUrl}{self.username}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                parse_data(response.json())
            else:
                print("Request failed")
        except Exception as e:
            print(f"An error occurred: {e}")