import random
from art import logo

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower() 
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    chosen_number = random.randint(1, 100)

    is_game_over = False
    while attempts > 0 and is_game_over == False:
        guess = int(input("Make a guess: "))

        if guess == chosen_number:
            print(f"You got it! The answer is {chosen_number}")
            is_game_over = True
        else:
            if guess > chosen_number:
                print("Too high.")
            else:
                print("Too low.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                is_game_over = True
            else:
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")

play_game()