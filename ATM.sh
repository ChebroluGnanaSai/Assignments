

initial_amount=10000


while true
do
    echo "Enter Your Choice"
    echo "1. Check Balance"
    echo "2. Deposit"
    echo "3. Withdraw"
    echo "4. Exit"

    echo "Enter your choice:"
    read a

    case $a in
        1)
            echo "Current Balance: $initial_amount"
            ;;
        2)
            echo "Enter Deposited Amount:"

            read deposited_amount
	    if [[$deposited_amount -gt >0 ]];then

	            initial_amount=$((initial_amount + deposited_amount))
		    echo "Updated Balance: $initial_amount"
	    else 
		    echo "Invalid Amount"
	    fi

            ;;
        3)
            echo "Enter Withdrawal Amount:"
            read withdraw_amount

            if [ $withdraw_amount -le $initial_amount ]; then
                initial_amount=$((initial_amount - withdraw_amount))
                echo "Updated Balance: $initial_amount"
            else
                echo "Insufficient Balance!"
            fi
            ;;
        4)
            echo "Thank you."
            exit 0
            ;;
        *)
            echo "Invalid Choice. Please try again."
            ;;
    esac
done
