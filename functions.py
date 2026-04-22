import random

def get_computer_choice():
    choices = ["stone", "paper", "scissor"]
    random_index = random.randint(0, 2)
    return choices[random_index]

def get_user_choice():
    choice = input("Enter your choice (stone, paper, scissor): ")
    return choice.lower()

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif user == "stone" and computer == "scissor":
        return "user"
    elif user == "paper" and computer == "stone":
        return "user"
    elif user == "scissor" and computer == "paper":
        return "user"
    else:
        return "computer"
