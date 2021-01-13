import random


def win():
    with open('win_riddle.txt', 'r') as file:
        x = file.readlines()
    choice = random.randint(0, len(x) - 1)
    print(x[choice])


def lose():
    with open('lose_riddle.txt', 'r') as file:
        x = file.readlines()
    choice = random.randint(0, len(x) - 1)
    print(x[choice])


def question():
    file1 = open('Riddle_Questions.txt', 'r')
    file2 = open('Riddle_Answers.txt', 'r')
    questions = file1.readlines()
    answers = file2.readlines()
    x = random.randint(0, len(questions) - 1)
    ques = questions[x]
    print(ques)
    user_ans = input('=')
    ans = answers[x]
    # check if ans is right
    if ans.rstrip() in user_ans:
        win()
    else:
        lose()


# main
def main():
    run = True
    while run:
        question()
        choice = input('Do you want another question ?(Y/N)')
        print()
        if choice in 'nN':
            run = False
