import random


def rpc_game(choice: int):
    """Rock Paper Scissors Game"""
    choices = ("rock", "paper", "scissor")
    user_choice = choice
    computer_choice = random.randint(1, 3)
    print(choices[user_choice-1])
    print(choices[computer_choice - 1])
    if (user_choice == computer_choice):
        print("Tie")
    elif (user_choice > computer_choice):
        if user_choice-computer_choice == 2:
            print(choices[computer_choice - 1], "wins")
        else:
            print(choices[user_choice - 1], "wins")
    elif (user_choice < computer_choice):
        if computer_choice-user_choice == 2:
            print(choices[user_choice - 1], "wins")
        else:
            print(choices[computer_choice - 1], "wins")








print("winning Rules of the Rock paper and scissor game as follows:", "\n", "rock vs paper->paper wins", "\n",
      "rock vs scissors->rock wins" "\n", "paper vs scissors->scissors wins ")
print("\n")
print("Enter choice", "\n", "1. Rock", "\n", "2. paper", "\n", "3. scissor ")
choice = int(input("Enter your choice:"))
print(rpc_game(choice))
k = input("Enter Y to continue playing and N to stop:")
while (k == "Y" or k=='y'):
    q = int(input("Enter your choice:"))
    rpc_game(q)
    k = input("Enter Y to continue playing and N to stop:")
