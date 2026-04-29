import numpy as np
from game import Game # Base Game Class
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) # To access modules from parent directory
import pygame
class Othello(Game):
    
    # Function which helps to show valid moves on the screen
    def valid_moves_show(self):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.validate_move(row, col):
                    valid_moves.append((row, col)) # If a move is valid, it gets added to valid_moves array
        for row, col in valid_moves:
            self.board[row][col] = 3 # Marking the valid move cells differently
    
    # Function to validate a move by going in all directions and checking if there is atleast one opponent disc between 2 current player's disc (including the specified one)
    def validate_move(self, row, col):
        if self.board[row][col] == 1 or self.board[row][col] == 2: # If already occupied, invalid
            return False
        opponent = 2 if self.turn == self.player1 else 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_disc = False
            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == opponent:
                    has_opponent_disc = True # A Marker which suggests that opponent disc was present in this direction before the current player's disc
                elif self.board[r][c] == (1 if self.turn == self.player1 else 2):
                    if has_opponent_disc: # Checks whether there was atleast one opponent disc between this cell and the first cell from which we started
                        return True
                    break
                else:
                    break # Because we encountered a null cell before another current player disc cell
                r += dr
                c += dc
        return False

    # Function which changes the board array values after a move is made
    def flip_discs(self, row, col):
        opponent = 2 if self.turn == self.player1 else 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            discs_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                discs_to_flip.append((r, c)) # Any opponent disc which is encountered before current player's disc will get added
                r += dr
                c += dc
            if 0<= r < 8 and 0 <= c < 8 and self.board[r][c] == (1 if self.turn == self.player1 else 2): # Checks if the last cell at which while loop breaks has current player's disc or not
                for rr, cc in discs_to_flip: 
                    self.board[rr][cc] = 1 if self.turn == self.player1 else 2 # Changing the values of the opponent disc's in between (essentially flipping)

    # Function which checks whether the current player has any valid moves left by simply looping all over the board and with the help of validate_move function
    def has_valid_moves(self):
        for row in range(8):
            for col in range(8):
                if self.validate_move(row, col):
                    return True # If atleast one valid move is left, returns True
        return False

    # IMPORTANT : THIS FUNCTION IS NOT THE ENTIRETY OF WIN CONDITION CHECK
    # Function which evaluates the winner only after the board is filled
    def check_win(self):
        if np.all(self.board != 0):
            player1_count = np.sum(self.board == 1) # Goes all over the board and adds up the boolean values (self.board==1), effectively counting the number of player 1 discs present
            player2_count = np.sum(self.board == 2)
            if player1_count > player2_count: # Basic check of who has more discs on board
                print(f"{self.player1} wins!")
                return 1
            elif player2_count > player1_count:
                print(f"{self.player2} wins!")
                return 2
            else:
                print("It's a tie!")
                return 3
        return -1 # If return value is not -1 , then winner variable will be changed accordingly

    # Kind of like the main function
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Othello")
        back = pygame.image.load("media/Othello/back_othello_og.png")
        background= pygame.transform.scale(back,(800,800)) # Scaling it to fit in the screen
        black_disc= pygame.image.load("media/Othello/black_disc_newbie.png")
        white_disc= pygame.image.load("media/Othello/white_disc_newbie.png")
        black_disc= pygame.transform.scale(black_disc,(100,100)) # Scaling to fit into a cell (8x8 board)
        white_disc= pygame.transform.scale(white_disc,(100,100))
        icon= pygame.image.load("media/Othello/othello_icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        running=True
        winner=-1 # Default winner value
        while running:
            screen.blit(background,(0,0)) # Background display
            self.valid_moves_show() # To mark valid moves
            x_coord,y_coord= pygame.mouse.get_pos()
            xx,yy= x_coord//100,y_coord//100 # To get in which row and col mouse is at
            if self.validate_move(yy,xx): # Hover effect when cursor is on a valid move cell
                pygame.draw.circle(screen,(180,255,180),(xx*100+50,yy*100+50),40,3) # Basic Hover effect by increasing radius and width, and changing colour
            # Loop which dynamically displays all discs on the board and valid moves
            for i in range(8):
                for j in range(8):
                    if self.board[i][j]==1:
                        screen.blit(black_disc,(j*100,i*100))
                    elif self.board[i][j]==2:
                        screen.blit(white_disc,(j*100,i*100))
                    elif self.board[i][j]==3:
                        pygame.draw.circle(screen,(80,200,80),(j*100+50,i*100+50),35,2) # Basic circle to represent valid moves
                        self.board[i][j]=0 # Changing it back to 0 to not disturb the code for check_win
            pygame.display.update() # Updates the board
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running= False # To stop running when close button is clicked on the window
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y= pygame.mouse.get_pos() # Gets the position where mouse was clicked (move made)
                    row=y//100
                    col=x//100
                    if self.turn==self.player1:
                        turn=1 # Using a variable which stores integer value and represent the current player
                    else:
                        turn=2
                    if self.validate_move(row,col): # Validation of move
                        self.board[row][col]=turn # Placing the disc mathematically
                        if turn==1:
                            screen.blit(black_disc,(col*100,row*100)) # Placing the disc visually
                        else:
                            screen.blit(white_disc,(col*100,row*100))
                        self.flip_discs(row, col) # Changing the array to represent the state of board after flipping discs
                        for i in range(8): # Flipping discs visually
                            for j in range(8):
                                if self.board[i][j]==1:
                                    screen.blit(black_disc,(j*100,i*100))
                                elif self.board[i][j]==2:
                                    screen.blit(white_disc,(j*100,i*100))
                        u=self.check_win() # Checking board fill win
                        pygame.display.update() # Displaying the final flip on board
                        if u!=-1: # If board is filled
                            winner = u # Winner variable representing winner directly
                            pygame.time.wait(3000) # Giving the players time to see what happened
                            return winner # Useful for display of results in the next window
                        self.switch() # Switching turns
                        # IMPORTANT : THIS IS LIKE THE SECOND PART OF WIN CONDITION CHECK
                        if not self.has_valid_moves(): # Checking if player after switching turn has valid moves left
                            print(f"{self.turn} has no valid moves. Skipping turn")
                            self.switch() # Switching turns because current player has no valid moves left
                            if not self.has_valid_moves(): # Checking if next player also has any moves left or not
                                print("No valid moves for both players. Ending game") # As no valid moves are left for both players, evaluating the winner
                                p1count = np.sum(self.board == 1) # Similar check as of the check_win one
                                p2count = np.sum(self.board == 2)
                                if p1count > p2count:
                                    print(f"{self.player1} wins!")
                                    winner = 1
                                elif p2count > p1count:
                                    print(f"{self.player2} wins!")
                                    winner = 2
                                else:
                                    print("It's a tie!")
                                    winner = 3
                                pygame.time.wait(3000)
                                return winner
                            
                    
        
        
            







