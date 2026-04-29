#!/bin/bash
echo "===============   Leaderboard for TicTacToe   ===============" # Code is similar for leaderboard of all games
echo "Player               Wins   Losses   Win/Loss Ratio"
echo "----------------------------------------------------" # Basic display which parallels a table

# For everyline in history.csv, there is a winner and a loser. So when awk is going through every line, it adds the wins and losses of players to specific associative arrays
# At the END, we will first go through the entries of players who have won atleast once (is present in wins array)
# Specifically, for Losses=0 case, keep W/L ratio as inf
# Reason for this is when leaderboard is sorted using g flag (general numeric sort), inf is treated as the largest value. So sorting becomes easier
# Then we will look for players who are only in losses array and print them
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
}' history.csv | # Now we sort
if [[ $1 == "1" ]]; then # First argument is the choice of sorting method
    sort -k2,2nr # Sorting by wins, so n flag (numeric sort) and r flag (reverse) because by default n flag gives results in increasing order
elif [[ $1 == "2" ]]; then
    sort -k3,3n # Similarly sorting by losses, but without r flag because player with least number of losses being on top of leaderboard makes more sense
else
    sort -k4,4gr # Sorting by W/L ratio and usage of g flag is already justified
fi
#Similar code for all the games
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
