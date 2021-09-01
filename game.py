import math
import time
from player import HumanPlayer, RandomComputerPlayer , GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to reperesent a 3 x 3 board
        self.current_winner = None #to keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '|'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc ( Tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '|'.join(row) + ' |')

    def available_moves(self):
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        # List comprehension of the same
        return [i for (i,spot) in enumerate(self.board) if spot == ' ']
    def empty_squares(self):
        return ' ' in self.board
    
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self,square,letter):
        #3 in a row anywhere is a winner - It can be a row , a column or a diagonal
        #first lets check row first
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #column next
        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #(diagonals are made up of 0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all of these if false
        return False



    

def play(game,x_player,o_player,print_game = True):
    #returns the winner [letter]if there is one , else returns None for tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game still has empty squares
    # (We don't have to worry about getting a winner because we will just return that)
    # Which breakes the loop
    while game.empty_squares():
        # getting move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter

            #after we make the move we need to alternate the letter
            letter = 'O' if letter == 'X' else 'X'
        time.sleep(1)


    if print_game:
        print('It\'s a tie!')        




if __name__ == "__main__":
    d = 'Y'
    while(d == 'Y'):
        x_player = GeniusComputerPlayer('X')
        o_player = HumanPlayer('O')
        t = TicTacToe()
        play(t,x_player,o_player,print_game=True)
        d = input("DO You want to play again press 'Y' for Yes and 'N' for No :  ")