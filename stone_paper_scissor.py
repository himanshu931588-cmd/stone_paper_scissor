import functions

def play_game():
    while True:
        print("\n--- Stone Paper Scissor ---")
        user_choice = functions.get_user_choice()
        
        if user_choice not in ["stone", "paper", "scissor"]:
            print("Invalid choice, try again.")
            continue
            
        computer_choice = functions.get_computer_choice()
        print("Computer chose: " + computer_choice)
        
        winner = functions.determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
        else:
            print("Computer wins!")
            
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

play_game()
