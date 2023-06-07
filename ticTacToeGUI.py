"""
Author:Mesoma Okolocha
Lab:10
File: ticTacToeGUI.py

Displays a window with multiple buttons and plays the connect four game.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from ticTacToe import TicTacToe

class TicTacToeGUI(EasyFrame):

   def __init__(self):
      """Creates the connect four game, sets up labels for each play space,
      buttons for each column, a current turn label, and a restart button."""
      super().__init__(title = "Tic Tac Toe!")
      self.game = TicTacToe()
      
      self.setSize(64 * len(self.game.board), 64 * len(self.game.board[0]))
      
      self.tokenImages = {
         "X" : PhotoImage(file = "x.png"),
         "O" : PhotoImage(file = "o.png"),
         " " : PhotoImage(file = "empty.png")
      }
      
      
      self.stateLabel = self.addLabel("Turn:", row = len(self.game.board) + 2, column = 0)
      self.turnLabel= self.addLabel("", row = len(self.game.board) + 2, column = 1)
      
      self.boardButtons = []
      
      for row in range(len(self.game.board)):
         self.boardButtons.append([])
         for column in range(len(self.game.board[row])):
            self.boardButtons[row].append(self.addButton("", row=row, column=column,command=self.makeColumnFunction(row,column)))
      
      self.setBoardButtons()
      
      self.columnButtons = []
      # Create a column button for each column, place them in the row len(self.game.board) + 2
      #for column in range(len(self.game.board[0])):
         #self.columnButtons.append(self.addButton(row=len(self.game.board)+1,column=column,
                                                  #text="{:^10d}".format(column),command=self.makeColumnFunction(row,column)))
      
      # Set the text of each one to the column number with "{:^10d}".format() to center the numbers
      # Set the command with the self.makeColumnFunction() method
      # Set the state to "normal"
   
      # Add a new game button to invoke self.newGame, with its state initially set to "disabled"
      self.newGameButton=self.addButton(row=len(self.game.board)+2, column=len(self.game.board)-1, text="New",
                                  command=self.newGame,state="disabled",columnspan=2)
      # Recommended columnspan is 2
      
      
   def makeColumnFunction(self,row,column):
      """Creates a function application using the column to pass as an argument
      to self.nextMove. Used by self.columnButtons."""
      
      return lambda: self.nextMove(row,column)
      
      
   def setBoardButtons(self):
      # Set the matching row,column label in boardLabels to the
      for row in range(len(self.game.board)):
         for column in range(len(self.game.board[row])):
            self.boardButtons[row][column]["image"]=self.tokenImages[self.game.board[row][column]]
         
      
      # appropriate image based on self.game.board's row,column
        
      # Set the image of the turnLabel to the correct image based on self.game.getTurn()
      self.turnLabel["image"]=self.tokenImages[self.game.getTurn()]
      
      # Temporary pass statement
      
      

   def nextMove(self,row,column):
      """Makes a move in the game and updates the view with
      the results."""
      
      
      # Call the step on the game with the given column
      self.game.step(row,column)
      
      self.setBoardButtons()
      
      # If the game is over, use self.messageBox to indicate who won, and
      if self.game.isGameOver():
         self.messageBox("Game over!",self.game.getTurn() + " Won!")
         for button in self.boardButtons:
             for b in button:
                 b["state"]="disabled"
         self.newGameButton["state"]="normal"
         
      #  set the state of all column buttons to "disabled", and set the
      #  state of the new game button to "normal"

   def newGame(self):
      """Create a new connect four game and updates the view."""
      # Set self.game to a new connect four game
      self.game=TicTacToe()
      self.setBoardButtons()
      
      # Set the state of the new game button to "disabled"
      self.newGameButton["state"]="disabled"
      # Set the state of all column buttons to "normal"
      for button in self.boardButtons:
          for b in button:
              b["state"]="normal"

def main():
   app = TicTacToeGUI()
   app.mainloop()

if __name__ == "__main__":
   main()

