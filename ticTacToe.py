
class TicTacToe(object):
    def __init__(self):
        self.board = [[" " for x in range(3)] for y in range(3)]    
        self.turn = 0
        self.tokens = ["X", "O"]
        self.gameOver = False
        
    def getTurn(self):
        return self.tokens[self.turn % 2]
    
    def isGameOver(self):
        return self.gameOver
    
    def step(self, row, column):
        
        # modify the self.board
        self.board[row][column] = self.tokens[self.turn % 2]

        # Manually check all possible wins
        if self.board[0][0] != " " and \
                self.board[0][0] == self.board[0][1] and \
                self.board[0][1] == self.board[0][2]:
            self.gameOver = True
        elif self.board[0][0] != " " and \
                  self.board[0][0] == self.board[1][0] and \
                  self.board[1][0] == self.board[2][0]:
            self.gameOver = True
        elif self.board[0][0] != " " and \
                  self.board[0][0] == self.board[1][1] and \
                  self.board[1][1] == self.board[2][2]:
            self.gameOver = True
        elif self.board[2][0] != " " and \
                  self.board[2][0] == self.board[1][1] and \
                  self.board[1][1] == self.board[0][2]:
            self.gameOver = True
        elif self.board[0][1] != " " and \
                  self.board[0][1] == self.board[1][1] and \
                  self.board[1][1] == self.board[2][1]:
            self.gameOver = True
        elif self.board[0][2] != " " and \
                  self.board[0][2] == self.board[1][2] and \
                  self.board[1][2] == self.board[2][2]:
            self.gameOver = True
        elif self.board[1][0] != " " and \
                  self.board[1][0] == self.board[1][1] and \
                  self.board[1][1] == self.board[1][2]:
            self.gameOver = True

        if not self.gameOver:
            self.turn += 1

    def display(self):
        print("\n-+-+-\n".join(["|".join(row) for row in self.board]))
        print()
    

if __name__ == "__main__":
    
    game = TicTacToe()
    
    while not game.isGameOver():
    
        game.display()
        row, column = input("Enter row and column separated by a space: ").split()        
    
        # ask for input
        row = int(row)
        column = int(column)
        
        game.step(row, column)
    
    print("game over!")
    game.display()
