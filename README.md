# MyChess

<p align="center">
    <img width="150" src="https://github.com/khalidbelk/MyChess/assets/72026317/0a516d8e-7f10-4cf8-ab08-199ba4ce8a87">
</p>

This project is a basic application created for experimenting with the **Chess.com public API**. It provides a simple command-line interface to interact with the API and retrieve information about users and their games.


## Requirements

Before using **mychess**, ensure you have the following installed on your system:

- Python 3
- Pip (Python package installer)


## Usage

First of all, compile the project at the root directory using the following command:
```
make
```
After building, the executable **mychess** will be generated. You can use it as follows:

```
./mychess -u user [gamesYear gamesMonth]
    user            is the Chess.com username. This flag alone provides information about the user.
    gamesYear       is the year of the user's games you want to download
    gamesMonth      is the month of the user's games you want to download
```
