import random

# List of words to choose from
words = ["giraffe", "elephant", "tiger", "lion"]

# Game loop (allows replay)
while True:
    
    # Randomly select a word
    secret_word = random.choice(words)
    
    # Initialize variables
    guess = ""
    attempts = 3

    print("\nWelcome to the Word Guessing Game!")
    print("You have 3 attempts to guess the correct word.")

    # Main game loop
    while guess != secret_word and attempts > 0:
        
        # Take input from user
        guess = input("Enter your guess: ").lower()

        # Check if guess is correct
        if guess == secret_word:
            print("You win! 🎉")
            break

        # Reduce attempts if incorrect
        attempts -= 1

        # Provide feedback
        if attempts > 0:
            print(f"Wrong guess! You have {attempts} attempts left.")
            
            # Give a hint (first letter)
            print(f"Hint: The word starts with '{secret_word[0]}'")
        else:
            print("You have no more attempts!")

    # If user failed to guess
    if guess != secret_word:
        print(f"You lose! The correct word was '{secret_word}'")

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break