# Define variables
balance = 0
is_running = True

def show_balance():
    print("*******************************************************")
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("*******************************************************")
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("*******************************************************")
        print("Withdraw amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    global balance
    global is_running

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("*******************************************************")
            print("That is not a valid option")

    print("Thank you! Have a nice day")

# Call main() function
main()
