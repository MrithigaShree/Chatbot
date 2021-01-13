import random


def main():
    move = ['rock', 'paper', 'scissor']
    run = True
    me = 0
    you = 0
    while run:
        a = random.randint(0, 2)
        x = move[a]
        print('******************************************')
        choice = input('''
Enter:-
rock/paper/scissor
0 - quit
score - to show score
= ''')
        if choice == '0':
            break
        if choice == 'score':
            print('Me:  ', me)
            print('You: ', you)
            continue
        print('My choice :', x)
        if x == choice:
            print('We tied!')
        elif a == 0 and choice == 'scissor':
            print('I win!')
            me += 1
        elif a == 1 and choice == 'rock':
            print('I win')
            me += 1
        elif a == 2 and choice == 'paper':
            print('I win!')
            me += 1
        else:
            if choice in ['rock', 'paper', 'scissor']:
                print('You win!')
                you += 1
            else:
                print('Wrong choice')
                continue

