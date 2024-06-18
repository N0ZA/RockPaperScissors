import random

while 1:
    choice = str(input("make your choice (rock/paper/scissors): "))
    choices = ["rock", "paper", "scissors"]
    opp = random.choice(choices)
    print("COM chooses " + opp)
    if choice in choices:
        if opp == choice:
            print("tie! try again")
            continue
        if choice == "rock":
            if opp == "paper":
                print("you lose")
                break
            elif opp == "scissors":
                print("you win")
                break
        if choice == "paper":
            if opp == "scissors":
                print("you lose")
                break
            elif opp == "rock":
                print("you win")
                break
        if choice == "scissors":
            if opp == "rock":
                print("you lose")
                break
            elif opp == "paper":
                print("you win")
                break
    else:
        print("type again")
exit()


