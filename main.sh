#!/bin/bash
LorR() {
        ##login or registration function
        while true; do
                #validating username
                read -p "Enter username: " name
                if [[ -z "${name// }" ]]; then
                        echo "Username cannot be empty.Try again." >&2
                        continue
                elif [[ "$un1" == "$name" ]]; then
                        echo "Username already taken by Player1. Please choose a different username." >&2
                        continue
                fi
                if  grep -qe "^$name\>" users.tsv; then
                        echo "Username exists" >&2
                        #checking password
                        while true; do
                                read -sp "Enter password:" password
                                echo "" >&2
                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}')
                                if grep -q "^$name[[:space:]]$hashed" users.tsv; then
                                        echo "Logged in successfully" >&2
                                        echo $name
                                        return 0
                                else
                                        echo "Password Incorrect" >&2
                                        read -p "Are you sure you are $name?(y/n)" variable
                                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                                continue
                                        else
                                                break
                                        fi
                                fi
                        done
                #registration process
                else
                        read -p "Username does not exist.Want to try registering?(y/n)" variable
                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                while true; do
                                        read -sp "Enter password:" password
                                        echo "" >&2
                                        read -sp "Confirm password:" cpassword
                                        echo "" >&2
                                        if [[ $password != $cpassword ]]; then
                                                echo "Passwords do not match.Try again" >&2
                                        else
                                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}')
                                                echo -e "$name\t$hashed" >> users.tsv
                                                read -p "Registration successful.Want to login with this credentials?(y/n)" variable1
                                                if [[ $variable1 == "y" || $variable1 == "Y" ]]; then
                                                        echo "Logged in successfully" >&2
                                                        echo $name
                                                        return 0
                                                else
                                                        echo "Taking you back to login interface" >&2
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
un1=$(LorR)
echo "<Player2>"
un2=$(LorR)
python3 game.py $un1 $un2
