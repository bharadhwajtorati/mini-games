
#importing necessary libraries
import subprocess
import pygame
import sys
import numpy as np
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#creating a class for the game which will be inherited by all the games
class Game:
    def __init__(self,player1,player2,n):
        self.player1=player1
        self.player2=player2
        self.turn=player1
        
        # initialising the board according to the game selected by the user
        if n==1:
            self.board=np.zeros((10,10),dtype=int)  #
        elif n==2:
            self.board=np.zeros((7,7),dtype=int)
        else:
            self.board=np.zeros((8,8),dtype=int)
            self.board[4,4]=2
            self.board[3,3]=2
            self.board[4,3]=1
            self.board[3,4]=1
         
        #function to switch the turn of players 
    def switch(self):
            self.turn=self.player1 if self.turn==self.player2 else self.player2     

#function to record the results of game(win/loss) in history.csv file 
#with the format : winner,loser,date_time,game_name
def record_results(un1,un2,gamename):
    with open("history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([un1, un2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),gamename])

#function to write text on the screen
def write(screen,str, x, y, colour=(0,0,0), font_size=50):
        font = pygame.font.SysFont(None, font_size) 
        text = font.render(str, True,colour)  
        screen.blit(text,(x, y))  

#stating interface for the menu of games         
def interface():
    
    #initialising pygame and loading necessary images,scaling for the menu
    pygame.init()
    menu=pygame.display.set_mode((1000,900))
    pygame.display.set_caption("Mini-Games")
    background_image=pygame.image.load("media/Interface/background.png").convert_alpha()
    background_image=pygame.transform.scale(background_image,(1000,900))
    tic_tac_toe_icon=pygame.image.load("media/Interface/tic-tac-toe_big.png").convert_alpha()
    tic_tac_toe_icon=pygame.transform.smoothscale(tic_tac_toe_icon,(290,290))
    ttt_rect = tic_tac_toe_icon.get_rect(topleft=(32,475))
    connect_four_icon=pygame.image.load("media/Interface/connect-four_big.png").convert_alpha()
    connect_four_icon=pygame.transform.smoothscale(connect_four_icon,(290,290))
    cf_rect = connect_four_icon.get_rect(topleft=(355,475))
    othello_icon=pygame.image.load("media/Interface/othello_big.png").convert_alpha()
    othello_icon=pygame.transform.smoothscale(othello_icon,(290,290))
    othello_rect = othello_icon.get_rect(topleft=(678,475))
    mini_game_bigicon=pygame.image.load("media/Interface/game_big.png").convert_alpha()
    mini_game_bigicon=pygame.transform.smoothscale(mini_game_bigicon,(750,300))
    mini_game_bigicon.set_colorkey((0,0,0))
    mini_game_icon=pygame.image.load("media/Interface/game.png")
    pygame.display.set_icon(mini_game_icon)
    running  = True
    game=0
    while running:
        
        #displaying the menu and updating the display according to the mouse position for the hover effect on the game icons
        menu.blit(background_image, (0, 0))
        menu.blit(mini_game_bigicon,(145,30))
        Mpos=pygame.mouse.get_pos()
        if ttt_rect.collidepoint(Mpos):
            menu.blit(pygame.transform.smoothscale(tic_tac_toe_icon,(300,300)),(27,470))
            menu.blit(connect_four_icon,(355,475))
            menu.blit(othello_icon,(678,475))
        elif cf_rect.collidepoint(Mpos):
            menu.blit(tic_tac_toe_icon,(32,475))
            menu.blit(pygame.transform.smoothscale(connect_four_icon,(300,300)),(350,470))
            menu.blit(othello_icon,(678,475))
        elif othello_rect.collidepoint(Mpos):
            menu.blit(tic_tac_toe_icon,(32,475))
            menu.blit(connect_four_icon,(355,475))
            menu.blit(pygame.transform.smoothscale(othello_icon,(300,300)),(673,470))
        else:
            menu.blit(tic_tac_toe_icon,(32,475))
            menu.blit(connect_four_icon,(355,475))
            menu.blit(othello_icon,(678,475))
        write(menu,"Tic-Tac-Toe",74,770,colour=(255,255,51),font_size=50) 
        write(menu,"Connect-Four",385,770,colour=(255,255,51),font_size=50)
        write(menu,"Othello",770,770,colour=(255,255,51),font_size=50)
        pygame.display.update()
        
        #responding to the mouse click events to launch the respective games and quitting the menu if the user clicks on the close button
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
    pygame.quit() #quitting before launching the game to use a single pygame window
    return game   #returning the game selected by the user to launch the respective game in the main function

#ending interface for showing the winner 
#and taking input for sorting the leaderboard according to wins/losses/win-loss ratio or quitting the leaderboard
def stats(winner):
    
    #initialising pygame and creating the layout for the stats interface with hover effect on the sorting options
    pygame.init()
    stats=pygame.display.set_mode((500,300))
    pygame.display.set_caption("Winner")
    rect1 = pygame.Rect(12, 180, 150, 60)
    rect_1=pygame.Rect(7, 178, 160, 64)
    rect2 = pygame.Rect(12+13+150, 180, 150, 60)
    rect_2= pygame.Rect(7+13+150, 178, 160, 64)
    rect3 = pygame.Rect(12+13+150+13+150, 180, 150, 60)
    rect_3= pygame.Rect(7+13+150+13+150, 178, 160, 64)
    running = True
    sort=0
    while running:
        
        #this part is resposible for the hover effect on the sorting options and updating the display accordingly
        stats.fill((30, 30, 47))
        write(stats,f"WINNER : {winner}",65,40,(255,215,0))
        write(stats,"Click sorting option for leaderboard:",10,120,font_size=35,colour=(180,190,210))
        Mpos=pygame.mouse.get_pos()
        if rect1.collidepoint(Mpos):
            pygame.draw.rect(stats, (42-6,42-6,64-7), rect_1, border_radius=21)
            write(stats,"Wins",12+31,180+14,font_size=53,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect2, border_radius=20)
            write(stats,"Losses",12+13+150+16,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect3, border_radius=20)
            write(stats,"Win/Loss",12+13+150+13+150+10,180+16,font_size=45,colour=(255,255,255))
        elif rect2.collidepoint(Mpos):
            pygame.draw.rect(stats, (42,42,64), rect1, border_radius=20)
            write(stats,"Wins",12+31,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42-6,42-6,64-7), rect_2, border_radius=21)
            write(stats,"Losses",12+13+150+16,180+14,font_size=53,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect3, border_radius=20)
            write(stats,"Win/Loss",12+13+150+13+150+10,180+16,font_size=45,colour=(255,255,255))
        elif rect3.collidepoint(Mpos):
            pygame.draw.rect(stats, (42,42,64), rect1, border_radius=20)
            write(stats,"Wins",12+31,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect2, border_radius=20)
            write(stats,"Losses",12+13+150+16,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42-6,42-6,64-7), rect_3, border_radius=21)
            write(stats,"Win/Loss",7+13+150+13+150+10,180+16,font_size=48,colour=(255,255,255))
        else :
            pygame.draw.rect(stats, (42,42,64), rect1, border_radius=20)
            write(stats,"Wins",12+31,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect2, border_radius=20)
            write(stats,"Losses",12+13+150+16,180+14,font_size=50,colour=(255,255,255))
            pygame.draw.rect(stats, (42,42,64), rect3, border_radius=20)
            write(stats,"Win/Loss",12+13+150+13+150+10,180+16,font_size=45,colour=(255,255,255))
            
        #taking input from the mouse click events to sort the leaderboard according to wins/losses/win-loss ratio or quitting the leaderboard
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                sort = 4
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
    return sort   #returning the sorting option selected by the user     

#function to plot the stats of the players and games played using matplotlib
def plot_stats():
    
    #getting the data from the history.csv file to pick the top 5 playes by wins and the distribution of games played
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
    
    #picking the top 5 players by wins and plotting the bar graph for top 5 players
    top5_players = list(sorted(wins.keys(), key=lambda x: wins[x], reverse=True))[:5]
    top5_wins = [wins[player] for player in top5_players]
    plt.figure(figsize=(12, 6))
    plt.subplot(1,2,1)
    plt.bar(top5_players, top5_wins)
    plt.xlabel("Players")
    plt.ylabel("Number of Wins")
    plt.title("Top 5 Players by Wins")
    plt.subplot(1,2,2)
    x_labels=list(counts.keys())
    y_values=list(counts.values())
    
    #plotting the pie chart for distribution of games played
    plt.pie(y_values, labels=x_labels,autopct='%2.1f%%')
    plt.title("Distribution of Games Played")
    plt.suptitle("Plots of Wins and Game distribution")
    plt.tight_layout()
    plt.show()

def main():
    #storing the names of 2 users
    un1= sys.argv[1]
    un2= sys.argv[2]
    print(f"Welcome to The Gaming Hub {un1} and {un2}")
    print("Opening the menu of games")
    while True:
        #showing the interface to choose the game 
        variable= interface()
        winner = None
        
        #running the respective game choosen and recording the results
        if variable == 1 :
            print("Launching Tic-Tac-Toe")
            from games.tic_tac_toe import TicTacToe
            ttt = TicTacToe(un1, un2, 1)
            winner = ttt.run()
            if winner == 1:
                record_results(un1,un2,"TicTacToe")
            elif winner == 2:
                record_results(un2,un1,"TicTacToe")   
        elif variable== 2 :
            print("Launching Connect_Four")
            from games.Connect_Four import ConnectFour
            CF = ConnectFour(un1, un2, 2)
            winner = CF.run()
            if winner == 1:
                record_results(un1,un2,"Connect_Four")
            elif winner == 2:
                record_results(un2,un1,"Connect_Four")  
        elif variable== 3 :
            print("Launching Othello")
            from games.othello import Othello
            OT=Othello(un1,un2,3)
            winner = OT.run()
            if winner == 1:
                record_results(un1,un2,"Othello")
            elif winner == 2:
                record_results(un2,un1,"Othello")
        elif variable== 4 :
            break
        
        #getting the option to sort the leaderborard or skip leaderboard
        sort_option=stats((un1 if winner == 1 else un2 if winner==2 else "Tie" if winner==3 else None))
        
        #running leaderloard.sh to show the leaderboard and showing plots
        if sort_option != 4:
            subprocess.run(f"bash leaderboard.sh {sort_option}", shell=True)   
            plot_stats()

        #asking do you want to play again or quit
        if input("do you want to play again(y/n)").lower() == "y" :
            continue
        else:
            print("Quitting menu")
            break           

if __name__=="__main__":   main()

