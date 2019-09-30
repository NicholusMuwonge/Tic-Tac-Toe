from beautifultable import BeautifulTable
import random


class Structure:

    # create how the board will display like in the terminal
    def __init__(self):
        self.table = BeautifulTable()

    def board_structure(self, board):
        table = BeautifulTable()
        # table represented by positional values
        table.append_row([board[7], board[8], board[9]])
        table.append_row([board[4], board[5], board[6]])
        table.append_row([board[1], board[2], board[3]])
        print(table)

    def welcome(self):
        print('Welcome to Tic Tac Toe, My Version!')


class Prompts:

    # add prompts for user to choose character
    def chooseCharacter(self):
        # choose letter
        letter = None
        while not (letter == 'Y' or letter == 'A'):
            print('Do you want to be Y or A?')
            letter = input().upper()
        # the index[0] is the player
        if letter == 'Y':
            return ['Y', 'A']
        else:
            return ['A', 'Y']


class Logic:

    # this is the class that holds all the logic to the game
    def __init__(self):
        self.boardLayout = Structure()
        self.prompt = Prompts()
    
    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'ai'
        else:
            return 'human'