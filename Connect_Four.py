import pygame
import numpy as np
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
        screen.fill((255, 255, 255))
        icon= pygame.image.load("connect-four.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Connect Four")
        
        player1img= pygame.image.load("redball.png")
        player1img = pygame.transform.scale(player1img, (80, 80))
        player2img= pygame.image.load("blueball.png")
        player2img = pygame.transform.scale(player2img, (135, 135))
        
        def draw_board():
            screen.blit(board, (-110, 60))
        def draw_balls():
            for i in range(7):
                for j in range(7):
                    if self.board[i, j] == 1:
                        redball(39+j*108,96*i+217)
                    elif self.board[i, j] == 2:
                        blueball(12+j*108,96*i+192)
      
        def redball(x,y):
            screen.blit(player1img,(x,y))
        def blueball(x,y):
            screen.blit(player2img,(x,y))
        def drop_redball(x,y):
                X=39+x*108
                Y=100
                for i in range(49):
                    screen.fill((255, 255, 255))
                    redball(X,Y)
                    draw_board()
                    draw_balls()
                    pygame.display.update()
                    pygame.time.wait(1)
                    Y+=2.4375+2*y
                self.board[row, col] = 1
        def drop_blueball(x, y):
                X=12+x*108
                Y=78
                for i in range(49):
                    screen.fill((255, 255, 255))
                    blueball(X,Y)
                    draw_board()
                    draw_balls()
                    pygame.display.update()
                    pygame.time.wait(1)
                    Y+=2.375+2*y
                self.board[row, col] = 2
                    
        board= pygame.image.load("connect four board.png")
       
        draw_board()
        running = True
        turn = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                            drop_redball(col, row)
                            if self.check_win(row, col)[0]:
                                print(f"{self.player1} wins!")
                                running = False
                                pygame.display.update()
                                pygame.time.wait(3000)
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
                            turn = 1
            pygame.display.update()
if __name__=="__main__":
    ConnectFour("Player1","Player2",2).run()   