import numpy as np
from game import Game
import pygame
class Othello(Game):
    def valid_moves_show(self):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.validate_move(row, col):
                    valid_moves.append((row, col))
        for row, col in valid_moves:
            self.board[row][col] = 3
    def validate_move(self, row, col):
        if self.board[row][col] == 1 or self.board[row][col] == 2:
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
                return 3
        return -1
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Othello")
        back = pygame.image.load("back_othello_og.png")
        background= pygame.transform.scale(back,(800,800))
        black_disc= pygame.image.load("black_disc_newbie.png")
        white_disc= pygame.image.load("white_disc_newbie.png")
        black_disc= pygame.transform.scale(black_disc,(100,100))
        white_disc= pygame.transform.scale(white_disc,(100,100))
        running=True
        winner=-1
        while running:
            screen.blit(background,(0,0))
            self.valid_moves_show()
            x_coord,y_coord= pygame.mouse.get_pos()
            xx,yy= x_coord//100,y_coord//100
            if self.validate_move(yy,xx):
                self.board[yy][xx]=4
                pygame.draw.circle(screen,(180,255,180),(xx*100+50,yy*100+50),40,3)
            pygame.display.update()
            for i in range(8):
                for j in range(8):
                    if self.board[i][j]==1:
                        screen.blit(black_disc,(j*100,i*100))
                    elif self.board[i][j]==2:
                        screen.blit(white_disc,(j*100,i*100))
                    elif self.board[i][j]==3:
                        pygame.draw.circle(screen,(80,200,80),(j*100+50,i*100+50),35,2)
                        self.board[i][j]=0
                    elif self.board[i][j]==4:
                        self.board[i][j]=0
            
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running= False
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
                                winner = 3
                            pygame.display.update()
                            pygame.time.wait(3000)
                            running = False
                            return winner
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
                                    winner = 3
                                pygame.display.update()
                                pygame.time.wait(3000)
                                running = False
                                return winner
                            
                    
        
        
            







