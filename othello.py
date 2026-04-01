import numpy as np
from game import Game
import pygame
class Othello(Game):
    def validate_move(self, row, col):
        if self.board[row][col] != 0:
            return False
        opponent = 2 if self.turn == self.player1 else 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_disc = False
            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == opponent:
                    has_opponent_disc = True
                elif self.board[r][c] == (1 if self.turn == self.player1 else 2):
                    if has_opponent_disc:
                        return True
                    break
                else:
                    break
                r += dr
                c += dc
        return False
    def flip_discs(self, row, col):
        opponent = 2 if self.turn == self.player1 else 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            discs_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                discs_to_flip.append((r, c))
                r += dr
                c += dc
            if 0<= r < 8 and 0 <= c < 8 and self.board[r][c] == (1 if self.turn == self.player1 else 2):
                for rr, cc in discs_to_flip:
                    self.board[rr][cc] = 1 if self.turn == self.player1 else 2
    def has_valid_moves(self):
        for row in range(8):
            for col in range(8):
                if self.validate_move(row, col):
                    return True
        return False
    def check_win(self):
        if np.all(self.board != 0):
            player1_count = np.sum(self.board == 1)
            player2_count = np.sum(self.board == 2)
            if player1_count > player2_count:
                print(f"{self.player1} wins!")
                return 1
            elif player2_count > player1_count:
                print(f"{self.player2} wins!")
                return 2
            else:
                print("It's a tie!")
                return 0
        return -1
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Othello")
        screen.fill((0,128,0))
        for i in range(1,8):
            pygame.draw.line(screen,(0,0,0),(i*100,0),(i*100,800),3)
            pygame.draw.line(screen,(0,0,0),(0,i*100),(800,i*100),3)
        black_disc= pygame.image.load("blackdisc.png")
        white_disc= pygame.image.load("white disc.png")
        black_disc= pygame.transform.scale(black_disc,(100,100))
        white_disc= pygame.transform.scale(white_disc,(100,100))
        for i in range(3,5):
            for j in range(3,5):
                if self.board[i][j]==1:
                    screen.blit(black_disc,(j*100,i*100))
                elif self.board[i][j]==2:
                    screen.blit(white_disc,(j*100,i*100))
        pygame.display.update()
        running=True
        winner=-1
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running= False
                    break 
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y= pygame.mouse.get_pos()
                    row=y//100
                    col=x//100
                    if self.turn==self.player1:
                        turn=1
                    else:
                        turn=2
                    if self.validate_move(row,col):
                        self.board[row][col]=turn
                        if turn==1:
                            screen.blit(black_disc,(col*100,row*100))
                        else:
                            screen.blit(white_disc,(col*100,row*100))
                        self.flip_discs(row, col)
                        for i in range(8):
                            for j in range(8):
                                if self.board[i][j]==1:
                                    screen.blit(black_disc,(j*100,i*100))
                                elif self.board[i][j]==2:
                                    screen.blit(white_disc,(j*100,i*100))
                        u=self.check_win()
                        if u!=-1:
                            if u == 1:
                                winner = 1
                            elif u == 2:
                                winner = 2
                            else:
                                winner = 0
                            pygame.display.update()
                            pygame.time.wait(3000)
                            running = False
                            break
                        pygame.display.update()
                        self.switch()
                        if not self.has_valid_moves():
                            print(f"{self.turn} has no valid moves. Skipping turn")
                            self.switch()
                            if not self.has_valid_moves():
                                print("No valid moves for both players. Ending game")
                                p1count = np.sum(self.board == 1)
                                p2count = np.sum(self.board == 2)
                                if p1count > p2count:
                                    print(f"{self.player1} wins!")
                                    winner = 1
                                elif p2count > p1count:
                                    print(f"{self.player2} wins!")
                                    winner = 2
                                else:
                                    print("It's a tie!")
                                    winner = 0
                                pygame.display.update()
                                pygame.time.wait(3000)
                                running = False
                                break
        pygame.quit()
        return winner
                            
                    
        
        
            







