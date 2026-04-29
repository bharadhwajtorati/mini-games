#!/bin/bash
# Function which handles with login and registration
LorR() {
        while true; do
                read -p "Enter username: " name # Prompts to enter a username
                if [[ -z "${name// }" ]]; then # Checks for empty username
                        echo "Username cannot be empty.Try again." >&2 # IMPORTANT : This format of >&2 can be seen throughout the function, majorly because we want only one output to get stored in the un1 and un2 variables (see later code to understand)
                        continue
                elif [[ "$un1" == "$name" ]]; then # Makes sure usernames are distinct
                        echo "Username already taken by Player1. Please choose a different username." >&2
                        continue
                fi
                if  grep -qe "^$name\>" users.tsv; then # Checks for username in users.tsv (q flag is for the grep to stay quiet and not print anything)
                        echo "Username exists" >&2
                        while true; do
                                read -sp "Enter password:" password # Prompting to enter password (s flag makes sure password isn't shown on screen when typing) 
                                echo "" >&2
                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}') # Final hashed value of password (Because sha256 command provides additional field)
                                if grep -q "^$name[[:space:]]$hashed" users.tsv; then # Verifying whether the password matches for the username
                                        echo "Logged in successfully" >&2
                                        echo $name # Returns the username as the password was correct
                                        return 0
                                else
                                        echo "Password Incorrect" >&2
                                        read -p "Are you sure you are $name?(y/n)" variable # To make sure a user doesn't accidentally type in wrong username and get stuck in a try password again loop
                                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                                continue # As user is sure about the username, taking them back to password prompt
                                        else
                                                break # As user typed in wrong username, taking them back to username prompt
                                        fi
                                fi
                        done
                else # Registration part of the function as username doesn't exist
                        read -p "Username does not exist.Want to try registering?(y/n)" variable
                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                while true; do
                                        read -sp "Enter password:" password # Prompting to enter password
                                        echo "" >&2
                                        read -sp "Confirm password:" cpassword # Prompting to confirm password 
                                        echo "" >&2
                                        if [[ $password != $cpassword ]]; then # Basic check whether the passwords match
                                                echo "Passwords do not match.Try again" >&2
                                        else
                                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}')
                                                echo -e "$name\t$hashed" >> users.tsv # Storing the username and hashed value of password in a tsv file
                                                read -p "Registration successful.Want to login with this credentials?(y/n)" variable1 # Maybe user is just trying to register in our famous game hub
                                                if [[ $variable1 == "y" || $variable1 == "Y" ]]; then
                                                        echo "Logged in successfully" >&2
                                                        echo $name # Returns username
                                                        return 0
                                                else
                                                        echo "Taking you back to login interface" >&2 # Taking them to username prompt because they don't want to login with this credentials
                                                fi
                                        fi
                                done

                        else
                                continue
                        fi
                fi
        done
}

echo "<Player1>"
un1=""
un1=$(LorR) # Only the final echo $name output will be stored into un1 because everything else will be displayed on screen (error messages)
echo "<Player2>"
un2=$(LorR) # Similar authentication process for 2nd player too
python3 game.py $un1 $un2 # Launching the game hub by passing two usernames of players as arguments
