import pygame
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from game import Game
class ConnectFour(Game):
    
    def validate_move(self, col):
        if self.board[0, col] == 0:
            return True
        else:
            return False
        
    def check_max(self ,player , row, col, x, y):
        if(row>6 or row<0 or col>6 or col<0):
            return 0
        if self.board[row, col] != player:
            return 0
        return 1+ self.check_max(player, row+y, col+x, x, y)

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
        return L

    def run(self):
        pygame.init()
        
        screen = pygame.display.set_mode((800, 900))
        screen.fill((0,0,0))
        icon= pygame.image.load("media/Connect_Four/connect-four.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Connect Four")
        
        player1img= pygame.image.load("media/Connect_Four/greenball.png")
        player1img = pygame.transform.scale(player1img, (133, 133)).convert_alpha()
        player2img= pygame.image.load("media/Connect_Four/blueball.png")
        player2img = pygame.transform.scale(player2img, (133, 133)).convert_alpha()
        
        def draw_board():
            screen.blit(board, (-110, 60))
        def draw_balls():
            for i in range(7):
                for j in range(7):
                    if self.board[i, j] == 1:
                        greenball(14+j*107,96*i+187)
                    elif self.board[i, j] == 2:
                        blueball(14+j*107,96*i+187)
      
        def greenball(x,y):
            screen.blit(player1img,(x,y))
        def blueball(x,y):
            screen.blit(player2img,(x,y))
        def drop_greenball(x,y):
                X=14+x*107
                Y=72
                for i in range(49):
                    screen.fill((0,0,0))
                    greenball(X,Y)
                    draw_balls()
                    draw_board()
                    pygame.display.update()
                    pygame.time.wait(5)
                    Y+=2.375+2*y
                self.board[row, col] = 1
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
                    pygame.time.wait(5)
                self.board[row, col] = 2
                    
        board= pygame.image.load("media/Connect_Four/CF_board.png").convert_alpha()
        winner = 0   
        draw_board()
        running = True
        turn = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y= pygame.mouse.get_pos()
                    button = event.button
                    if button != 1:
                        continue
                    col = x//114
                    if self.validate_move(col):
                        if turn == 1:
                            row = 6
                            while self.board[row, col] != 0:
                                row -= 1
                            drop_greenball(col, row)
                            if self.check_win(row, col)[0]:
                                print(f"{self.player1} wins!")
                                running = False
                                pygame.display.update()
                                pygame.time.wait(3000)
                                winner = 1
                            turn = 2 
                        else:
                            row = 6
                            while self.board[row, col] != 0:
                                row -= 1
                            drop_blueball(col, row)
                            if self.check_win(row, col)[0]:
                                print(f"{self.player2} wins!")
                                running = False
                                pygame.display.update()
                                pygame.time.wait(3000)
                                winner = 2
                            turn = 1
                    trash=pygame.event.get()
                            
            pygame.display.update()
            if not np.any(self.board == 0):
                print("It's a draw!")
                pygame.time.wait(3000)
                winner = 3
        pygame.quit()    
        return winner
    
if __name__=="__main__":
    ConnectFour("Player1","Player2",2).run()   