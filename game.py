import pygame
import sys
import numpy as np
import csv
from datetime import datetime

class Game:
    def __init__(self,player1,player2,n):
        self.player1=player1
        self.player2=player2
        self.turn=player1
        if n==1:
            self.board=np.zeros((10,10),dtype=int)
        elif n==2:
            self.board=np.zeros((7,7),dtype=int)
        else:
            self.board=np.zeros((8,8),dtype=int)
            self.board[4,4]=2
            self.board[3,3]=2
            self.board[4,3]=1
            self.board[3,4]=1
    def switch(self):
        if self.turn == self.player1:
            self.turn=self.player2
        else:
            self.turn = self.player1

        
def record_results(un1,un2,gamename):
    with open("history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([un1, un2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),gamename])

def interface():
    pygame.init()
    
    screen=pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Mini-Games")
    screen.fill((135,206,255))
    def write(str, x, y, colour=(0,0,0), font_size=50, font=None):
        font = pygame.font.SysFont(None, font_size) 
        text_surface = font.render(str, True,colour)  
        screen.blit(text_surface,(x, y))
        
    tic_tac_toe_icon=pygame.image.load("tic-tac-toe_big.png")
    screen.blit(tic_tac_toe_icon,(50,500))
    write("Tic-Tac-Toe",74,770)
    
    connect_four_icon=pygame.image.load("connect-four_big.png")
    screen.blit(connect_four_icon,(400,500))
    write("Connect-Four",425,772)

    othello_icon=pygame.image.load("othello_big.png")
    othello_icon=pygame.transform.smoothscale(othello_icon,(290,290))
    write("Othello",805,770)

    mini_game_bigicon=pygame.image.load("game_big.png")
    screen.blit(mini_game_bigicon,(255,100))
    write("Mini-Games",380,130,font_size=100)
    
    screen.blit(othello_icon,(720,490))
    
    mini_game_icon=pygame.image.load("game.png")
    pygame.display.set_icon(mini_game_icon)
    
    pygame.display.update()
    
    running  = True
    game=0
    while running:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
                game = 4
                print("Quitting menu")
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y= event.pos
                    if(y>=500 and y<=800):
                        if(50<=x<=300):
                            game = 1
                            running=False
                            break
                        elif( 400 <= x <= 660 ):
                            game=2
                            running=False
                            break
                        elif(740<=x<=990):
                            game=3
                            running=False
                            break
    pygame.quit()
    return game                  
              
def main():
    from tic_tac_toe import TicTacToe
    from Connect_Four import ConnectFour
    from othello import Othello
    
    un1= sys.argv[1]
    un2= sys.argv[2]
    print(f"Welcome to The Gaming Hub {un1} and {un2}")
    print("Opening the menu of games")
    while True:
        variable= interface()
        winner = None
        if variable == 1 :
            print("Launching Tic-Tac-Toe")
            ttt = TicTacToe(un1, un2, 1)
            winner = ttt.run()
            if winner == 1:
                record_results(un1,un2,"TicTacToe")
            elif winner == 2:
                record_results(un2,un1,"TicTacToe")
        elif variable== 2 :
            print("Launching Connect_Four")
            CF = ConnectFour(un1, un2, 2)
            winner = CF.run()
            if winner == 1:
                record_results(un1,un2,"Connect_Four")
            elif winner == 2:
                record_results(un2,un1,"Connect_Four")
            
        elif variable== 3 :
            print("Launching Othello")
            OT=Othello(un1,un2,3)
            winner = OT.run()
            if winner == 1:
                record_results(un1,un2,"Othello")
            elif winner == 2:
                record_results(un2,un1,"Othello")
            
        elif variable== 4 :
            variable1=input("Are you sure you want to quit?(y/n)\n")
            if variable1 == "y" or variable1 == "Y":
                print("Quitting the menu")
                break
            else:
                print("Try again")
                continue
        else:
            print("Invalid choice.Try again")
        
        
        
            
if __name__=="__main__":
    main()


