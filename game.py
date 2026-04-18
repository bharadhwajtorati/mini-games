import pygame
import sys
import numpy as np
import csv
from datetime import datetime
import os
from matplotlib import pyplot as plt

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

def write(screen,str, x, y, colour=(0,0,0), font_size=50, font=None):
        font = pygame.font.SysFont(None, font_size) 
        text_surface = font.render(str, True,colour)  
        screen.blit(text_surface,(x, y))
        
def interface():
    pygame.init()
    
    menu=pygame.display.set_mode((1000,900))
    pygame.display.set_caption("Mini-Games")
    background_image=pygame.image.load("background.png")
    background_image=pygame.transform.scale(background_image,(1000,900))
    menu.blit(background_image, (0, 0))
        
    tic_tac_toe_icon=pygame.image.load("tic-tac-toe_big.png")
    tic_tac_toe_icon=pygame.transform.smoothscale(tic_tac_toe_icon,(290,290))
    menu.blit(tic_tac_toe_icon,(32,475))
    write(menu,"Tic-Tac-Toe",74,770,colour=(255,255,51),font_size=50)

    connect_four_icon=pygame.image.load("connect-four_big.png")
    connect_four_icon=pygame.transform.smoothscale(connect_four_icon,(290,290))
    menu.blit(connect_four_icon,(355,475))
    write(menu,"Connect-Four",385,770,colour=(255,255,51),font_size=50)

    othello_icon=pygame.image.load("othello_big.png")
    othello_icon=pygame.transform.smoothscale(othello_icon,(290,290))
    write(menu,"Othello",770,770,colour=(255,255,51),font_size=50)

    mini_game_bigicon=pygame.image.load("game_big.png")
    mini_game_bigicon.set_colorkey((0,0,0))
    mini_game_bigicon=pygame.transform.smoothscale(mini_game_bigicon,(750,300))
    menu.blit(mini_game_bigicon,(145,100))
    
    menu.blit(othello_icon,(678,475))
    
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
                    if(y>=475 and y<=475+290):
                        if(32<=x<=322):
                            game = 1
                            running=False
                            break
                        elif(355<=x<=645):
                            game=2
                            running=False
                            break
                        elif(678<=x<=968):
                            game=3
                            running=False
                            break
    pygame.quit()
    return game   

def stats(winner):
    pygame.init()
    
    stats=pygame.display.set_mode((500,300))
    stats.fill((30, 30, 47))
    pygame.display.set_caption("Winner")
    write(stats,f"WINNER : {winner}",65,40,(255,215,0))
    write(stats,"Click sorting option for leaderboard:",10,120,font_size=35,colour=(180,190,210),font="Roboto")
    
    rect = pygame.Rect(12, 180, 150, 60)
    pygame.draw.rect(stats, (42,42,64), rect, border_radius=20)
    write(stats,"Wins",12+31,180+14,font_size=50,colour=(255,255,255))
    
    rect = pygame.Rect(12+13+150, 180, 150, 60)
    pygame.draw.rect(stats, (42,42,64), rect, border_radius=20)
    write(stats,"Losses",12+13+150+16,180+14,font_size=50,colour=(255,255,255))

    rect = pygame.Rect(12+13+150+13+150, 180, 150, 60)
    pygame.draw.rect(stats, (42,42,64), rect, border_radius=20)
    write(stats,"Win/Loss",12+13+150+13+150+10,180+16,font_size=45,colour=(255,255,255))
    
    pygame.display.update()
    running = True
    sort=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                break
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    if 180<= y <= 240 :
                        if 12<= x<= 162:
                            sort = 1
                            running =False
                            break
                        elif 175<= x<= 325:
                            sort = 2
                            running =False
                            break
                        elif 338 <= x<= 488:
                            sort = 3
                            running =False
                            break
        
    pygame.quit()
    return sort         
              
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
            
            sort_option=stats((un1 if winner == 1 else un2 if winner==2 else "Tie" if winner==3 else None))
            os.system(f"bash leaderboard.sh 1 {sort_option}")
            
        elif variable== 2 :
            print("Launching Connect_Four")
            CF = ConnectFour(un1, un2, 2)
            winner = CF.run()
            if winner == 1:
                record_results(un1,un2,"Connect_Four")
            elif winner == 2:
                record_results(un2,un1,"Connect_Four")
            sort_option=stats((un1 if winner == 1 else un2 if winner==2 else "Tie" if winner==3 else None))
            os.system(f"bash leaderboard.sh 2 {sort_option}")
            
        elif variable== 3 :
            print("Launching Othello")
            OT=Othello(un1,un2,3)
            winner = OT.run()
            if winner == 1:
                record_results(un1,un2,"Othello")
            elif winner == 2:
                record_results(un2,un1,"Othello")
                
            sort_option=stats((un1 if winner == 1 else un2 if winner==2 else "Tie" if winner==3 else None))
            os.system(f"bash leaderboard.sh 3 {sort_option}")
            
        elif variable== 4 :
            variable1=input("Are you sure you want to quit?(y/n)\n")
            if variable1 == "y" or variable1 == "Y":
                print("Quitting the menu")
                break
            else:
                print("Try again")
                continue
        file=open("history.csv","r")
        wins={}
        counts={"TicTacToe":0,"Connect_Four":0,"Othello":0}
        for line in file:
            split=line.strip().split(",")
            winner=split[0]
            wins[winner] = wins.get(winner, 0) + 1
            if split[3]=="TicTacToe":
                counts[split[3]] += 1
            elif split[3]=="Connect_Four":
                counts[split[3]] += 1
            elif split[3]=="Othello":
                counts[split[3]] += 1
        file.close()
        top5_players = list(sorted(wins.keys(), key=lambda x: wins[x], reverse=True))[:5]
        top5_wins = [wins[player] for player in top5_players]
        plt.subplot(1,2,1)
        plt.bar(top5_players, top5_wins)
        plt.xlabel("Players")
        plt.ylabel("Number of Wins")
        plt.title("Top 5 Players by Wins")
        plt.subplot(1,2,2)
        x_labels=list(counts.keys())
        y_values=list(counts.values())
        plt.pie(y_values, labels=x_labels, autopct='%1.1f%%')
        plt.title("Distribution of Games Played")
        plt.suptitle("Plots of Wins and Game distribution")
        plt.tight_layout()
        plt.show()
        if input("do you want to play again(y/n)").lower() == "y" :
            continue
        else:
            print("Quitting menu")
            break
                 
if __name__=="__main__":
    main()
