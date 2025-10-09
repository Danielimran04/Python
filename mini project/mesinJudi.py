import random

def spin_row(): # tugas dia untuk buat output dari symbol and amik 3 sahaja(in range 3) lepastu masukkan dlm results variable
    symbols = ['🍒','🍉','🔔','⭐','🍋']

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):# nih just output balik dari result and cantikkan sikit 
    print("****************")
    print(" | ".join(row)) # join nih maksud dia kita boleh edit dlm list symbols[] sbb dlm list symbols[] tu kan ade buah je so guna join method maybe boleh tambah | or ape ape sahaja
    print("****************")


def get_payout(row, bet): # nih bila dpt tiga tiga sama sbb ape aku letak row[0] sbb aku dh set if row[0] == row[1] == row[2] so guna je salah satu
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
        
    return 0

def main():
    balance = 100

    print("****************************")
    print("Welcom to python slots")
    print("Symbols:🍒 🍉 🔔 ⭐ 🍋")
    print("****************************")

    while balance > 0:
        print(f"Current balance: RM{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number ")
            continue
    
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
    
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f"You won RM{payout}")
        else:
            print("Sorry you lost this round")
        
        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("***************************************************")
    print(f"Game over! Your final balance is RM{balance}")
    print("***************************************************")



if __name__=='__main__':
    main()
