# MINI-GAMES
A small game hub where you can play basic two-player games

## Table of Contents 
- [About](#about)
- [Games](games)
  - [Tic-Tac-Toe](#tic-tac-toe)
  - [Connect-Four](#connect-four)
  - [Othello](#othello)
- [Installation](#installation)
- [Usage](#usage)

## About
Building a secure, multi-user game hub that integrates Bash scripting for authentication and Python
(Pygame) for gameplay. Two authenticated players select a game from a menu, play via a
graphical interface, and have their results recorded on a persistent leaderboard.
## Games
This repository contains the following games

- Tic-Tac-Toe
- Connect-Four
- Othello

**Note:-** These games do not contain undo option.So play carefully. 

Here is their brief description
### Tic-Tac-Toe
---
- Played on a 10×10 board
- Players alternate placing X or O in any empty cell
- players need 5 marks in a row to win
- The winning line can be horizontal, vertical, or diagonal
- The game ends in a draw if the board fills with no winner
### Connect-Four
---
- Played on a vertical 7×7 grid
- Players take turns dropping one ball into any column
- ball fall to the lowest empty row in a column
- A player wins by getting 4 of their balls in a row (horizontal, vertical, or diagonal)
- The game ends in a draw if the board fills with no winner

### Othello
---
- Played on an 8×8 board, starting with two Black and two White discs in the centre
- A move is valid only if it traps one or more opponent discs in a straight line between the
newly placed disc and an existing own disc
- All trapped discs are flipped to the current player’s colour; multiple lines can be flipped in
one move
- If a player has no valid moves, their turn is skipped
- The player with more discs of their colour when no valid moves remain wins


## Installation
```bash
git clone https://github.com/user/repo.git
cd repo
pip install -r requirements.txt
```

## Usage
follow the instructions

- Start with this in the terminal
```bash
bash main.sh
```
- Then a interface pops up showing the 3 games

- Choose a game by a leftclick on the game and play it

- You can make your move by left-clicking on the box where you want to place it


- You can quit in middle by closing the window

- After the game completes, a small window appears asking you to choose the sorting option for the leaderboard 

- You can view the leaderboard in the terminal and also see a matplotlib graph in a separate window

- You can also skip leaderboard by closing the window

- You can replay or quit by following the instructions in the terminal


### Thank You
---
Thanks for taking the time to explore this project.I hope you like it.
### Enjoy playing
---