#!/bin/bash
if [[ $1 == "1" ]]; then
    game="TicTacToe"
elif [[ $1 == "2" ]]; then
    game="Othello"
else
    game="Connect4"
fi
echo "===============   Leaderboard for $game   ==============="
echo "Player               Wins   Losses   Win/Loss Ratio"
awk -F "," -v game="$game" ' 
$4==game {Ws[$1]++; Ls[$2]++} 
END {
    for (player in Ws) {
        if(Ls[player] == 0){
            ratio = "inf";
            printf("%-20s %-6d %-8d %-8s\n", player, Ws[player], Ls[player], ratio)
        } else {
            ratio = Ws[player] / Ls[player]
            printf("%-20s %-6d %-8d %-8.2f\n", player, Ws[player], Ls[player], ratio)
        }
        }
    for (player in Ls) {
        if (!(player in Ws)) {
            printf("%-20s %-6d %-8d %-8.2f\n", player, 0, Ls[player], 0)
        }
    }
}' history.csv | 
if [[ $2 == "1" ]]; then
    sort -k2,2nr
elif [[ $2 == "2" ]]; then
    sort -k3,3n
else
    sort -k4,4gr
fi

