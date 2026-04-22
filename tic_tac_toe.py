import pygame
import numpy as np
from game import Game
class TicTacToe(Game):
    def check_max(self ,player , row, col, x, y):
        if(row>9 or row<0 or col>9 or col<0):
            return 0
        if self.board[row, col] != player:
            return 0
        return 1+ self.check_max(player, row+y, col+x, x, y)
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
    
    def validate_move(self, row, col):
        if self.board[row, col] == 0:
            return True
        else:
            return False
        
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 800))
        icon= pygame.image.load("tic-tac-toe.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Tic-Tac-Toe")
        background_img = pygame.image.load("tic-tac-toe-back.png").convert_alpha()
        background_img = pygame.transform.scale(background_img, (800, 800))
        screen.blit(background_img, (0, 0))
        X_img=pygame.transform.scale(pygame.image.load("X.png"), (150, 150)).convert_alpha()
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
        def draw_blueline(x1, y1, x2, y2):
            pygame.draw.line(screen, (0, 150, 255), (x1, y1), (x2, y2), 10)
            pygame.draw.line(screen, (0, 245, 255), (x1, y1), (x2, y2), 7)
            pygame.draw.line(screen, (200, 255, 255), (x1, y1), (x2, y2), 3)
        def draw_greenline(x1, y1, x2, y2):
            pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 10)
            pygame.draw.line(screen, (0, 255, 80), (x1, y1), (x2, y2), 7)
            pygame.draw.line(screen, (180, 255, 180), (x1, y1), (x2, y2), 3)       
        running = True
        turn = 1
        winner = 0 
        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    break
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    button= event.button
                    
                    if button != 1:
                        continue
                    
                    if turn == 1:
                        if draw_x(x//80, y//80):
                            turn = 0
                            self.board[y//80, x//80] = 1
                            X=self.check_win(y//80, x//80)
                            if X[0]:
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
                        break
                    else:
                        if draw_o(x//80*80+40, y//80*80+40):
                            turn = 1
                            self.board[y//80, x//80] = 2
                            X=self.check_win(y//80, x//80)
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
                trash=pygame.event.get()
            pygame.display.update()
            if not np.any(self.board == 0):
                print("It's a draw!")
                pygame.time.wait(3000)
                running = False 
                winner = 3
        pygame.quit()        
        return winner
    
if __name__ == "__main__":
    ttt = TicTacToe("Player 1", "Player 2", 1)
    ttt.run()
