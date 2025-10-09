# python banking program

def show_balance(balance):
    print(f"Your balance is RM{balance:.2f}")

def deposit(balance):
    amount = float(input("Enter an amount to be deposited: "))

    if amount<0:
        print("Thats not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount=float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("In sufficient funds")
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
        print("\nBanking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        
        choice=input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running=False
        else:
            print("Invalid choice\n")

    print("\nTHANK YOUU HAVE A NICE DAY!!!")

if __name__ == '__main__':
    main()

