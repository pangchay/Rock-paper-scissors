import random

rock = "rock"
paper = "paper"
scissors = "scissors"
go_again = ""

print("Hello! Lets play a game of rock, paper, Scissors")
guess = input("please pick one now: ")

print("Jan...")
print("Ken...")
print("HO!")

npc_choices = ["rock", "paper", "scissors"]

npc_answer = random.choice(npc_choices)
print(npc_answer)

if npc_answer == "paper" and guess == "rock":
    print("You loose, better luck next time!")
elif npc_answer == "paper" and guess == "scissors":
    print("You win! Congratulations!")
elif npc_answer == "paper" and guess == "paper":
    print("my guess was also", npc_answer)
    print("Tie!")

elif npc_answer == "rock" and guess == "scissors":
    print("You loose, better luck next time!")
elif npc_answer == "rock" and guess == "paper":
    print("You win! Congratulations!")
elif npc_answer == "rock" and guess == "rock":
    print("Tie!")
    print("my guess was also", npc_answer)

elif npc_answer == "scissors" and guess == "paper":
    print("You loose, better luck next time!")
elif npc_answer == "scissors" and guess == "rock":
    print("You win! Congratulations!")
elif npc_answer == "scissors" and guess == "scissors":
    print("Tie!")
    print("my guess was", npc_answer)

go_again = (input("would you like to go again? Yes or no: "))

while go_again == "yes":
    npc_answer = random.choice(npc_choices)
    second_guess = input("Please pick again: ")
    print("Jan...")
    print("Ken...")
    print("HO!")
    print(npc_answer)

    if npc_answer == "paper" and second_guess == "rock":
        print("You loose, better luck next time!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "paper" and second_guess == "scissors":
        print("You win! Congratulations!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "paper" and second_guess == "paper":
        print("Tie!")
        go_again = (input("would you like to go again? Yes or no: "))

    elif npc_answer == "rock" and second_guess == "scissors":
        print("You loose, better luck next time!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "rock" and second_guess == "paper":
        print("You win! Congratulations!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "rock" and second_guess == "rock":
        print("Tie!")
        go_again = (input("would you like to go again? Yes or no: "))

    elif npc_answer == "scissors" and second_guess == "paper":
        print("You loose, better luck next time!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "scissors" and second_guess == "rock":
        print("You win! Congratulations!")
        go_again = (input("would you like to go again? Yes or no: "))
    elif npc_answer == "scissors" and second_guess == "scissors":
        print("Tie!")

        go_again = (input("would you like to go again? Yes or no: "))

else:
    print("Ok, Bye!")

    
