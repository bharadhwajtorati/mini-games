#!/bin/bash
echo "===============   Leaderboard for TicTacToe   ==============="
echo "Player               Wins   Losses   Win/Loss Ratio"
echo "----------------------------------------------------"
awk -F "," -v game="TicTacToe" ' 
$4~game {Ws[$1]++; Ls[$2]++} 
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
if [[ $1 == "1" ]]; then
    sort -k2,2nr
elif [[ $1 == "2" ]]; then
    sort -k3,3n
else
    sort -k4,4gr
fi
echo "===============   Leaderboard for Othello   ==============="
echo "Player               Wins   Losses   Win/Loss Ratio"
echo "----------------------------------------------------"
awk -F "," -v game="Othello" ' 
$4~game {Ws[$1]++; Ls[$2]++} 
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
if [[ $1 == "1" ]]; then
    sort -k2,2nr
elif [[ $1 == "2" ]]; then
    sort -k3,3n
else
    sort -k4,4gr
fi
echo "===============   Leaderboard for Connect_Four   ==============="
echo "Player               Wins   Losses   Win/Loss Ratio"
echo "----------------------------------------------------"
awk -F "," -v game="Connect_Four" ' 
$4~game {Ws[$1]++; Ls[$2]++} 
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
if [[ $1 == "1" ]]; then
    sort -k2,2nr
elif [[ $1 == "2" ]]; then
    sort -k3,3n
else
    sort -k4,4gr
fi
