LorR(){
        while true; do
                read -p "Enter username:" name
                if grep -q "^$name[[:space:]]" users.tsv; then
                        echo "Username exists"
                        while true; do
                                read -p "Enter password:" password
                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}')
                                if grep -q "^$name[[:space:]]$hashed" users.tsv; then
                                        echo "Logged in successfully"
                                        echo $name
                                        break 2
                                else
                                        echo "Password Incorrect"
                                        echo "Are you sure you are $name?(y/n)"
                                        read variable
                                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                                continue
                                        else
                                                break
                                        fi
                                fi
                        done
                else
                        echo "Username does not exist.Want to try registering?(y/n)"
                        read variable
                        if [[ $variable == "y" || $variable == "Y" ]]; then
                                while true; do
                                        read -p "Enter password:" password
                                        read -p "Confirm password:" cpassword
                                        if [[ $password != $cpassword ]]; then
                                                echo "Passwords do not match.Try again"
                                        else
                                                hashed=$(echo -n "$password" | sha256sum | awk '{print $1}')
                                                echo -e "$name\t$hashed" >> users.tsv
                                                echo "Registration successful.Want to login with this credentials?(y/n)"
                                                read variable1
                                                if [[ $variable1 == "y" || $variable1 == "Y" ]]; then
                                                        echo "Logged in successfully"
                                                        echo $name
							break 2
                                                else
                                                        echo "Taking you back to login interface"
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
un1=$(LorR)
echo "<Player2>"
un2=$(LorR)

