import random

rock = "rock"
paper = "paper"
scissors = "scissors"
go_again = "yes"
print("Hello! Lets play a game of rock, paper, Scissors")

while go_again == "yes" or "Yes" or "y" or "Y":

    npc_choices = ["rock", "paper", "scissors"]
    npc_answer = random.choice(npc_choices)
    guess = input("please pick one now: ")
    print("Jan...")
    print("Ken...")
    print("HO!")

    if npc_answer == "paper" and guess == "rock":
        print(f"My choice was {npc_answer}")
        print("You loose, better luck next time!")
    elif npc_answer == "paper" and guess == "scissors":
        print(f"My choice was {npc_answer}")
        print("You win! Congratulations!")
    elif npc_answer == "paper" and guess == "paper":
        print("my guess was also", npc_answer)
        print("Tie!")

    elif npc_answer == "rock" and guess == "scissors":
        print(f"My choice was {npc_answer}")
        print("You loose, better luck next time!")
    elif npc_answer == "rock" and guess == "paper":
        print(f"My choice was {npc_answer}")
        print("You win! Congratulations!")
    elif npc_answer == "rock" and guess == "rock":
        print("Tie!")
        print("my guess was also", npc_answer)

    elif npc_answer == "scissors" and guess == "paper":
        print(f" My choice was {npc_answer}")
        print("You loose, better luck next time!")
    elif npc_answer == "scissors" and guess == "rock":
        print(f" My choice was {npc_answer}")
        print("You win! Congratulations!")
    elif npc_answer == "scissors" and guess == "scissors":
        print("Tie!")
        print("my guess was", npc_answer)

    go_again = (input("would you like to go again? Yes or no: "))

else:
    print("Ok, Bye!")
