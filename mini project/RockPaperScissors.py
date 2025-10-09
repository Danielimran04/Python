import random
option = ("rock","paper","scissors")

is_running = True

while is_running:
    player = None
    computer = random.choice(option)
    player = input("Enter a choice (rock,paper,scissors): ").lower()
    while player not in option:
        player = input("Enter a choice (rock,paper,scissors): ").lower()
    print(f"COMPUTER: {computer}")
    print(f"Player: {player}")
    if player == computer:
        print("Its Draw!")
    elif player == "paper" and computer == "rock":
        print("You Win !")
    elif player == "rock" and computer == "scissors":
        print("You Win !")
    elif player == "scissors" and computer == "paper":
        print("You Win !")
    else:
        print("You lose!")
        
    play_again = input("Do you want to play again (y/n): ").lower()
    if play_again=="n":
        is_running=False


