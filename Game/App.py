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

    def winningCombo(self, board, letter):
        a = board
        b = letter
        return (
            (a[7] == b and a[8] == b and a[9] == b) or  
            (a[4] == b and a[5] == b and a[6] == b) or  
            (a[1] == b and a[2] == b and a[3] == b) or  
            (a[7] == b and a[4] == b and a[1] == b) or  
            (a[8] == b and a[5] == b and a[2] == b) or  
            (a[9] == b and a[6] == b and a[3] == b) or  
            (a[7] == b and a[5] == b and a[3] == b) or  
            (a[9] == b and a[5] == b and a[1] == b))


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

    def playAgain(self):
        # boolean with true/false response
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


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

    def recordMove(self, board, letter, move):
        board[move] = letter

    def updatedBoard(self, board):
        # get current board state.
        updatedBoard = []
        for key in board:
            updatedBoard.append(key)
        return updatedBoard

    def freeSpaces(self, board, move):
        # Return true if the passed move is free on the passed board.
        return (board[move] == ' ')

    def itsATie(self, board):
        # Return True if board is full.
        # Otherwise return False.
        for i in range(1, 10):
            if self.freeSpaces(board, i):
                return False
        return True

    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.freeSpaces(
            board, int(move)
                ):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def getComputerMove(self, board, ai):
        # Given a board and the computer's letter, determine
        # where to move and return that move.
        if ai == 'Y':
            human = 'A'
        else:
            human = 'Y'

        # Ai alogrith I got from Invent with Python by Al Sweigart
        # and used it
        for i in range(1, 10):
            copy = self.updatedBoard(board)
            if self.freeSpaces(copy, i):
                self.recordMove(copy, ai, i)
                if self.boardLayout.winningCombo(copy, ai):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = self.updatedBoard(board)
            if self.freeSpaces(copy, i):
                self.recordMove(copy, human, i)
                if self.boardLayout.winningCombo(copy, human):
                    return i

        # Try to take one of the corners, if they are free.
        # move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        possibleMoves = []
        for i in [1, 3, 7, 9]:
            if self.freeSpaces(board, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)

        # Try to take the center, if it is free.
        if self.freeSpaces(board, 5):
            return 5

        # Move on one of the sides.
        possibleMoves = []
        for i in [2, 4, 6, 8]:
            if self.freeSpaces(board, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)

    def executor(self):
        while True:
            # Set the board to blank fields
            theBoard = [' '] * 10
            human, ai = self.prompt.chooseCharacter()
            turn = self.whoGoesFirst()
            print('You\'re up' + turn + '.')
            inSession = True
            while inSession:
                if turn == 'human':
                    # human's turn.
                    self.boardLayout.board_structure(theBoard)
                    move = self.getPlayerMove(theBoard)
                    self.recordMove(theBoard, human, move)

                    if self.boardLayout.winningCombo(theBoard, human):
                        self.boardLayout.board_structure(theBoard)
                        print('Looks like I under estimated you pal!')
                        inSession = False
                    else:
                        if self.itsATie(theBoard):
                            self.boardLayout.board_structure(theBoard)
                            print('Rerun that mate!')
                            break
                        else:
                            turn = 'ai'

                else:
                    # ai's turn.
                    move = self.getComputerMove(theBoard, ai)
                    self.recordMove(theBoard, ai, move)
                    if self.boardLayout.winningCombo(theBoard, ai):
                        self.boardLayout.board_structure(theBoard)
                        print('Chin Up, this isnt certainly the best you could do.')
                        inSession = False
                    else:
                        if self.itsATie(theBoard):
                            self.boardLayout.board_structure(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'human'

            if not self.prompt.playAgain():
                print('Dont be no stranger now')
                break


Logic().boardLayout.welcome()
Logic().executor()
