

def show_balance(balance):
    print(f"your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be Deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the withdraw Amount"))

    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print("**************************")
        print("   Banking program   ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("!!!!!!!!!!!!!!!")
            print("That is an invalid choice")
            print("**********************")
    print("****************************")
    print("Thank you have a nice Day!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
if __name__ == '__main__':
    main()
