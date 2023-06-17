import random

def hangman():
    words = ['python', 'programming', 'hangman', 'code', 'computer', 'game']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"
        
        print("\nGuess the word:", hidden_word)
        print("Attempts remaining:", attempts)
        
        if hidden_word == word:
            print("\nCongratulations! You guessed the word correctly!")
            break
        
        if attempts == 0:
            print("\nGame Over! You ran out of attempts.")
            print("The word was:", word)
            break
        
        guess = input("Enter a letter: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing Hangman!")

hangman()
