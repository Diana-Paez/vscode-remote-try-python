import random

def play_round():
    """
    Plays one round of rock, paper, scissors game.
    Returns:
        1 if the user wins,
        -1 if the user loses,
        0 if it's a tie.
    """
    items = ["rock", "paper", "scissors"]
    computer_choice = random.choice(items)
    user_choice = input("Choose rock, paper or scissors: ").lower()

    if user_choice not in items:
        print("Invalid choice.")
        return 0

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1

def play_game():
    score = 0
    while True:
        result = play_round()
        score += result

        if result != 0:
            print(f"Your current score: {score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Final score: {score}")
            break

if __name__ == "__main__":
    play_game()
