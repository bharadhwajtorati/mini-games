#importing necessary libraries
import pygame
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..")) #to also search in the parent directory (outside the games folder)
from game import Game

#creating tic-tac-toe game class containing the game and all functions required to run it
class TicTacToe(Game):
    
    """check_max is a function that gives the maximum number of positions in a 
    particular direction from a given position that have the same item consecutively,
    matching the item at the given position. It is based on recursion."""
    def check_max(self ,player , row, col, x, y):
        if(row>9 or row<0 or col>9 or col<0):
            return 0
        if self.board[row, col] != player:
            return 0
        return 1+ self.check_max(player, row+y, col+x, x, y)
    
    """It checks the win condition by adding the check_max values of opposite directions 
    (for 4 possible directions) and returns data to identify where the win occurred."""
    def check_win(self, row, col):
        player = self.board[row, col]
        if self.check_max(player, row, col, 1, 0)+self.check_max(player, row, col, -1, 0) >= 6:
            L=[True,"E",self.check_max(player, row, col, 1, 0)-1, self.check_max(player, row, col, -1, 0)-1]   
        elif self.check_max(player, row, col, 0, 1)+self.check_max(player, row, col, 0, -1 ) >= 6:
            L= [True,"S",self.check_max(player, row, col, 0, 1)-1, self.check_max(player, row, col, 0, -1)-1]
        elif self.check_max(player, row, col, 1, 1)+self.check_max(player, row, col, -1, -1) >= 6:
            L= [True,"SE",self.check_max(player, row, col, 1, 1)-1, self.check_max(player, row, col, -1, -1)-1]
        elif self.check_max(player, row, col, -1, 1)+self.check_max(player, row, col, 1, -1) >= 6:
            L= [True,"SW",self.check_max(player, row, col, -1, 1)-1, self.check_max(player, row, col, 1, -1)-1]
        else :
            L= [False]
        return L 
    
    #checks whether the move is valid or not
    def validate_move(self, row, col):
        if self.board[row, col] == 0:
            return True
        else:
            return False
    
    #main game interface   
    def run(self):
        
        #initialising pygame and setting up display window
        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        
        #loading icon and setting window caption
        icon= pygame.image.load("media/Tic_Tac_Toe/tic-tac-toe.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Tic-Tac-Toe")
        
        #loading and scaling background image
        background_img = pygame.image.load("media/Tic_Tac_Toe/tic-tac-toe-back.png").convert_alpha()
        background_img = pygame.transform.scale(background_img, (800, 800))
        screen.blit(background_img, (0, 0)) #setting background
        
        #loading and scaling X image
        X_img=pygame.transform.scale(pygame.image.load("media/Tic_Tac_Toe/X.png"), (150, 150)).convert_alpha()
        
        #functions to draw X, O, and lines on the board
        def draw_x(x, y):
            if self.validate_move(y, x):
                screen.blit(X_img, (x*80-32, y*80-32))
                return True
            return False
        
        def draw_o(x, y):
            if self.validate_move(y//80, x//80):
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 30, width=5)
                pygame.draw.circle(screen, (0,255, 80), (x, y), 31, width=4)
                pygame.draw.circle(screen, (180, 255, 180), (x, y), 33, width=2)
                return True
            return False
        
        #draw blue line for player 1 win
        def draw_blueline(x1, y1, x2, y2):
            pygame.draw.line(screen, (0, 150, 255), (x1, y1), (x2, y2), 10)
            pygame.draw.line(screen, (0, 245, 255), (x1, y1), (x2, y2), 7)
            pygame.draw.line(screen, (200, 255, 255), (x1, y1), (x2, y2), 3)
        
        #draw green line for player 2 win
        def draw_greenline(x1, y1, x2, y2):
            pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 10)
            pygame.draw.line(screen, (0, 255, 80), (x1, y1), (x2, y2), 7)
            pygame.draw.line(screen, (180, 255, 180), (x1, y1), (x2, y2), 3)       
        
        running = True
        turn = 1
        winner = 0 
        
        #main game loop
        while running:
            
            #handling events: mouse input and quit
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    break
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    button= event.button
                    
                    if button != 1:
                        continue
                    
                    #player 1 move
                    if turn == 1:
                        
                        #draw X if valid, update board, check win, then switch turn
                        if draw_x(x//80, y//80):
                            self.board[y//80, x//80] = 1
                            X=self.check_win(y//80, x//80)
                            
                            #check for win
                            if X[0]:
                                
                                #drawing the line where the win occurs
                                print(f"{self.player1} wins!")
                                if(X[1] == "E"):
                                    draw_blueline((x//80+X[2])*80+40, y//80*80+40, (x//80-X[3])*80+40, y//80*80+40)
                                elif(X[1] == "S"):
                                    draw_blueline(x//80*80+40, (y//80+X[2])*80+40, x//80*80+40, (y//80-X[3])*80+40)
                                elif(X[1] == "SE"):
                                    draw_blueline((x//80+X[2])*80+40, (y//80+X[2])*80+40, (x//80-X[3])*80+40, (y//80-X[3])*80+40)
                                elif(X[1] == "SW"):
                                    draw_blueline((x//80-X[2])*80+40, (y//80+X[2])*80+40, (x//80+X[3])*80+40, (y//80-X[3])*80+40)
                                pygame.display.update()
                                pygame.time.wait(2000)
                                running = False
                                winner = 1
                            else:
                                turn=0
                        break
                    
                    #player 2 move (similar logic as player 1)
                    else:
                        if draw_o(x//80*80+40, y//80*80+40):
                            turn = 1
                            self.board[y//80, x//80] = 2
                            X=self.check_win(y//80, x//80)
                            
                            #check for win
                            if X[0]:
                                print(f"{self.player2} wins!")
                                if(X[1] == "E"):
                                    draw_greenline((x//80+X[2])*80+40, y//80*80+40, (x//80-X[3])*80+40, y//80*80+40)
                                elif(X[1] == "S"):
                                    draw_greenline(x//80*80+40, (y//80+X[2])*80+40, x//80*80+40, (y//80-X[3])*80+40)
                                elif(X[1] == "SE"):
                                    draw_greenline((x//80+X[2])*80+40, (y//80+X[2])*80+40, (x//80-X[3])*80+40, (y//80-X[3])*80+40)
                                elif(X[1] == "SW"):
                                    draw_greenline((x//80-X[2])*80+40, (y//80+X[2])*80+40, (x//80+X[3])*80+40, (y//80-X[3])*80+40)
                                pygame.display.update()
                                pygame.time.wait(2000)
                                running=False
                                winner = 2
                        break
                
                #clearing extra events
                trash=pygame.event.get()
            
            pygame.display.update()
            
            #checking for a draw (no empty cells left)
            if not np.any(self.board == 0):
                print("It's a draw!")
                pygame.time.wait(3000)
                running = False 
                winner = 3
        
        pygame.quit()        
        return winner #returning the winner
    
if __name__ == "__main__":
    ttt = TicTacToe("Player 1", "Player 2", 1)
    ttt.run()