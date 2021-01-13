import random


def word_get():
    pass
    # give user choice of theme
    # return word.txt
    count = 1
    print('Enter choice of theme')
    for i in ['Continents', 'Countries', 'Capital cities in India']:
        print(count, i)
        count += 1
    x = int(input('= '))
    if x == 1:
        file = open('continents.txt', 'r')
    elif x == 2:
        file = open('countries.txt', 'r')
    elif x == 3:
        file = open('Capital_cities_of_india.txt', 'r')
    else:
        print('wrong choice')
        word_get()
    # getting word.txt
    word_list = file.readlines()
    index = random.randint(0, len(word_list) - 1)
    word = word_list[index]
    word = word.rstrip()  # to remove \n or \r
    return word.upper()


def play(word):
    word_completion = "." * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word.txt: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.txt.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word.txt!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "." not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word.txt", guess)
            elif guess != word:
                print(guess, "is not the word.txt.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word.txt! You win!")
    else:
        print("Sorry, you ran out of tries. The word.txt was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    print('DON"T ENTER SPACES')
    word = word_get()
    play(word)
    while input("Play Again? (Y/N) ") in "yY":
        word = word_get()
        play(word)


if __name__ == "__main__":
    main()
