#Importing necessary libraries
import pygame
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) #To also search in the parent directory
from game import Game

#Creating Connect Four game class containing the game and all required functions
class ConnectFour(Game):
    
    #Checks whether a move is valid (column should not be full)
    def validate_move(self, col):
        if self.board[0, col] == 0:
            return True
        else:
            return False
        
    """Check_max returns the maximum number of consecutive positions 
    in a given direction from a position that match the same player.
    It is implemented using recursion."""
    def check_max(self ,player , row, col, x, y):
        if(row>6 or row<0 or col>6 or col<0):
            return 0  #Stops if index is out of range
        if self.board[row, col] != player:
            return 0  #Stops if a mismatch is found
        return 1+ self.check_max(player, row+y, col+x, x, y)

    """Checks the win condition by combining values from opposite directions
    (horizontal, vertical, and diagonals) and returns data about the win"""
    def check_win(self, row, col):
        player = self.board[row, col]
        if self.check_max(player, row, col, 1, 0)+self.check_max(player, row, col, -1, 0) >= 5:
            L=[True,"E",self.check_max(player, row, col, 1, 0)-1, self.check_max(player, row, col, -1, 0)-1]   
        elif self.check_max(player, row, col, 0, 1)+self.check_max(player, row, col, 0, -1 ) >= 5:
            L= [True,"S",self.check_max(player, row, col, 0, 1)-1, self.check_max(player, row, col, 0, -1)-1]
        elif self.check_max(player, row, col, 1, 1)+self.check_max(player, row, col, -1, -1) >= 5:
            L= [True,"SE",self.check_max(player, row, col, 1, 1)-1, self.check_max(player, row, col, -1, -1)-1]
        elif self.check_max(player, row,col,-1 , 1)+self.check_max(player,row,col , 1 , -1) >=5:
            L= [True,"SW",self.check_max(player,row,col,-1 , 1)-1,self.check_max(player,row,col , 1 , -1)-1]
        else :
            L= [False]
        return L #Returns whether there is a win, and if yes, its direction and distances

    #Main game interface
    def run(self):
        pygame.init()
        
        #Setting up display window and basic properties
        screen = pygame.display.set_mode((800, 900))
        screen.fill((0,0,0))
        
        #Loading icon and setting window caption
        icon= pygame.image.load("media/Connect_Four/connect-four.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Connect Four")
        
        #Loading and scaling player pieces
        player1img= pygame.image.load("media/Connect_Four/greenball.png")
        player1img = pygame.transform.scale(player1img, (133, 133)).convert_alpha()
        player2img= pygame.image.load("media/Connect_Four/blueball.png")
        player2img = pygame.transform.scale(player2img, (133, 133)).convert_alpha()
        board= pygame.image.load("media/Connect_Four/CF_board.png").convert_alpha()
        
        #Draws the board image
        def draw_board():
            screen.blit(board, (-110, 60))
        
        #Draws all placed balls based on current board state
        def draw_balls():
            for i in range(7):
                for j in range(7):
                    if self.board[i, j] == 1:
                        greenball(14+j*107,96*i+187)
                    elif self.board[i, j] == 2:
                        blueball(14+j*107,96*i+187)
      
        #Draws a green ball at the given position
        def greenball(x,y):
            screen.blit(player1img,(x,y))
        
        #Draws a blue ball at the given position
        def blueball(x,y):
            screen.blit(player2img,(x,y))
        
        #Animation for dropping a green ball into a column
        def drop_greenball(x,y):
                #Initial position
                X=14+x*107
                Y=72
                
                #Gradually increasing Y so it appears as falling
                for i in range(49):
                    screen.fill((0,0,0))
                    
                    #Redraw all balls and board to avoid artifacts
                    greenball(X,Y)
                    draw_balls()
                    draw_board()
                    pygame.display.update()
                    if(y>=4): pygame.time.wait(2)
                    pygame.time.wait(5) #Pause to control falling speed
                    Y+=2.375+2*y
                self.board[row, col] = 1
        
        #Animation for dropping a blue ball into a column (similar to green ball)
        def drop_blueball(x, y):
                X=14+x*107
                Y=72
                for i in range(49):
                    screen.fill((0,0,0))
                    blueball(X,Y)
                    draw_balls()
                    draw_board()
                    pygame.display.update()
                    Y+=2.375+2*y
                    if(y>=4): pygame.time.wait(2)
                    pygame.time.wait(5)
                self.board[row, col] = 2
                    
        winner = 0   
        draw_board()
        running = True
        turn = 1
        
        #Main game loop
        while running:
            #Handling events: mouse input and quit
            for event in pygame.event.get():
                
                #Handling quit event
                if event.type == pygame.QUIT:
                    running = False
                    break
                
                #Handling mouse click for moves
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y= pygame.mouse.get_pos() #Getting mouse position and button
                    button = event.button 
                    
                    if button != 1: #Ensures only left-click is processed
                        continue
                    
                    col = x//114
                    
                    #Check if move is valid before dropping
                    if self.validate_move(col):
                        
                        #Player 1 move
                        if turn == 1:
                            row = 6
                            
                            #Find lowest empty position in the column
                            while self.board[row, col] != 0:
                                row -= 1
                            
                            drop_greenball(col, row)
                            
                            #Check for win
                            if self.check_win(row, col)[0]:
                                print(f"{self.player1} wins!")
                                running = False
                                pygame.display.update()
                                pygame.time.wait(2000)
                                winner = 1
                            
                            turn = 2 #Switching turn
                        
                        #Player 2 move (similar logic)
                        else:
                            row = 6
                            while self.board[row, col] != 0:
                                row -= 1
                            
                            drop_blueball(col, row)
                            
                            if self.check_win(row, col)[0]:
                                print(f"{self.player2} wins!")
                                running = False
                                pygame.display.update()
                                pygame.time.wait(2000)
                                winner = 2
                            
                            turn = 1
                    
                    #Clearing extra events
                    trash=pygame.event.get()
                            
            pygame.display.update()
            
            #Checking for draw (no empty spaces left)
            if not np.any(self.board == 0):
                print("It's a draw!")
                pygame.time.wait(2000)
                winner = 3
        
        pygame.quit()    
        return winner #Returns 1 if player 1 wins, 2 if player 2 wins, 3 if draw, and 4 if quit in the middle
    
if __name__=="__main__":
    ConnectFour("Player1","Player2",2).run() #Run separately