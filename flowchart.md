Start by printing "Welcome to the Number Guessing Game!" to console.
Then, print "I'm thinking of a number between 1 and 100."
ask for input "Choose a difficulty. Type 'easy or 'hard': "
 if easy, remaining attempt is 10. if hard, remaining attempt is 5. default to hard.

repeat inside while loop as long as 1. user didn't guess right and 2. there are remaining attempts

    print "You have 10 attempts remaining to guess the number."
    ask for input "Make a guess: " wrap in int()

    if guess is equal to number, print "You got it! The answer is {chosen number}", program ends.

    if user guess is higher than chosen number, print "Too high.".
    if guess is lower than chosen number, print "Too low.".
    decrease remaining attempt by 1. if no more attempts left, print "You've run out of guesses, you lose."

    print "Guess again." 
    print "You have {remaining attempts} attempts remaining to guess the number." 
    
    
