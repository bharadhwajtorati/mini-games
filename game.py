import sys
import numpy as np

def main():
    un1= sys.argv[1]
    un2= sys.argv[2]
    print(f"Welcome to The Gaming Hub {un1} and {un2}")
    print("Opening the menu of games")
    while True:
        print("Select one game by typing the corresponding number as input")
        print("1.Tic-Tac-Toe")
        print("2.Othello")
        print("3.Connect4")
        print("4.Quit the menu")
        variable= input("Enter your choice: ")

        if variable == "1" :
            print("Launching Tic-Tac-Toe")

        elif variable== "2" :
            print("Launching Othello")

        elif variable== "3" :
            print("Launching Connecct4")
          
        elif variable== "4" :
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

