import random


def game(n):
    l = ["rock", "paper", "scissor"]
    n1 = random.randint(1, 3)
    print(n1)
    st = l[n - 1]
    st1 = l[n1 - 1]
    print(st)
    print(st1)
    if ((st == "rock" and st1 == "paper") or (st1 == "rock" and st == "paper")):
        print("paper wins")
    elif ((st == "rock" and st1 == "scissor") or (st1 == "rock" and st == "scissor")):
        print("rock wins")
    elif ((st == "paper" and st1 == "scissor") or (st1 == "paper" and st == "scissor")):
        print("scissor wins")
    elif (st == st1):
        print("Tie")


print("winning Rules of the Rock paper and scissor game as follows:", "\n", "rock vs paper->paper wins", "\n",
      "rock vs scissors->rock wins" "\n", "paper vs scissors->scissors wins ")
print("\n")
print("Enter choice", "\n", "1. Rock", "\n", "2. paper", "\n", "3. scissor ")
n = int(input("Enter your choice:"))
print(game(n))
k = input("Enter Y to continue playing and N to stop:")
while (k == "Y"):
    q = int(input("Enter your choice:"))
    print(game(q))
    k = input("Enter Y to continue playing and N to stop:")



