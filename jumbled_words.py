import random
def main():
    W = open("word.txt", 'r')
    WORDS = W.read().splitlines()

    #  pick one word randomly from the sequence
    word = random.choice(WORDS)
    # create a variable to use later to see if the guess is correct
    correct = word

    # create a jumbled version of the word
    jumble = ""

    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    W.close()

    # start the game
    print(
        """
                   Welcome to Word Jumble!
     
      Unscramble the letters to make a word.
      Enter a guess, an X to give up, or type ? and press enter for a hint.
      """)
    print()
    print("The jumble is:", jumble)
    print()
    guess = input("Your guess: ")
    guess = guess.lower()
    lst = range(len(jumble))
    hint_str = '_' * len(jumble)

    while True:

        if guess == correct:
            print("CORRECT!!")
            print()
            break
        elif guess == '?':
            i = random.choice(lst)
            print(correct[i], "is the", i + 1, "letter.")
            guess = input("Guess or '?' or 'X': ").lower()
        elif guess == 'x':
            print("Sorry you gave up!")
            print(correct, ' was the answer')
            break
        else:
            print("Sorry, thats not it. Try again.")
            guess = input("Guess or '?' or 'X': ").lower()

    print("GAME ENDED!!")
