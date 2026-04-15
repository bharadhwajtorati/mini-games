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
        screen.fill((255, 255, 255))
        icon= pygame.image.load("tic-tac-toe.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Tic-Tac-Toe")
        for i in range(1,10):
            pygame.draw.line(screen, (0, 0, 0), (i*80, 0), (i*80, 800), 5)
            pygame.draw.line(screen, (0, 0, 0), (0, i*80), (800, i*80), 5)
            
        def draw_x(x, y):
            if self.validate_move(y//80, x//80):
                pygame.draw.line(screen, (255, 0, 0), (x+28, y+28), (x-28, y-28), 15)
                pygame.draw.line(screen, (255, 0, 0), (x+28, y-28), (x-28, y+28), 15)
        def draw_o(x, y):
            if self.validate_move(y//80, x//80):
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 32, 15)
        
        running = True
        turn = 1
        winner = 0 
        while running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    button= event.button
                    
                    if button != 1:
                        continue
                    
                    if turn == 1:
                        draw_x(x//80*80+40, y//80*80+40)
                        turn = 0
                        self.board[y//80, x//80] = 1
                        X=self.check_win(y//80, x//80)
                        if X[0]:
                            print(f"{self.player1} wins!")
                            if(X[1] == "E"):
                                pygame.draw.line(screen, (255, 0, 0), ((x//80+X[2])*80+40, y//80*80+40), ((x//80-X[3])*80+40, y//80*80+40), 20)
                            elif(X[1] == "S"):
                                pygame.draw.line(screen, (255, 0, 0), (x//80*80+40, (y//80+X[2])*80+40), (x//80*80+40, (y//80-X[3])*80+40), 20)
                            elif(X[1] == "SE"):
                                pygame.draw.line(screen, (255, 0, 0), ((x//80+X[2])*80+40, (y//80+X[2])*80+40), ((x//80-X[3])*80+40, (y//80-X[3])*80+40), 20)
                            elif(X[1] == "SW"):
                                pygame.draw.line(screen, (255, 0, 0), ((x//80-X[2])*80+40, (y//80+X[2])*80+40), ((x//80+X[3])*80+40, (y//80-X[3])*80+40), 20)
                            pygame.display.update()
                            pygame.time.wait(3000)
                            running = False
                            winner = 1
                        break
                    else:
                        draw_o(x//80*80+40, y//80*80+40)
                        turn = 1
                        self.board[y//80, x//80] = 2
                        X=self.check_win(y//80, x//80)
                        if X[0]:
                            print(f"{self.player2} wins!")
                            if(X[1] == "E"):
                                pygame.draw.line(screen, (0, 0, 255), ((x//80+X[2])*80+40, y//80*80+40), ((x//80-X[3])*80+40, y//80*80+40), 20)
                            elif(X[1] == "S"):
                                pygame.draw.line(screen, (0, 0, 255), (x//80*80+40, (y//80+X[2])*80+40), (x//80*80+40, (y//80-X[3])*80+40), 20) 
                            elif(X[1] == "SE"): 
                                pygame.draw.line(screen, (0, 0, 255), ((x//80+X[2])*80+40, (y//80+X[2])*80+40), ((x//80-X[3])*80+40, (y//80-X[3])*80+40), 20)
                            elif(X[1] == "SW"):
                                pygame.draw.line(screen, (0, 0, 255), ((x//80-X[2])*80+40, (y//80+X[2])*80+40), ((x//80+X[3])*80+40, (y//80-X[3])*80+40), 20)
                            pygame.display.update()
                            pygame.time.wait(3000)
                            running=False
                            winner = 2
                        break
                
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
