# simple math game
import random

score = 0


def addition(x, y, z):
    global score
    sum1 = int(input('What is {} + {} = '.format(x, y)))
    if sum1 == x + y:
        score += z
    else:
        print('WRONG,it was {}\nyou lose {} points'.format(x + y, z))
        score -= z


def subtraction(x, y, z):
    global score
    dif1 = int(input('What is {} - {} = '.format(x, y)))
    if dif1 == (x - y):
        score += z
    else:
        print('WRONG,it was {}\nyou lose {} points'.format(x - y, z))
        score -= z


def multiplication(x, y, z):
    global score
    mul1 = float(input('What is {} * {} = '.format(x, y)))
    if mul1 == (x * y):
        score += z
    else:
        print('WRONG,it was {}\nyou lose {} points'.format(x * y, z))
        score -= z


def division(x, y, z):
    global score
    div1 = float(input('What is {} / {} = '.format(x, y)))
    if div1 == (x / y):
        score += z
    else:
        print('WRONG,it was {}\nyou lose {} points'.format(x / y, z))
        score -= z


def easy(n):
    for i in range(n):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        z = random.randint(0, 1)
        # addition
        if z == 0:
            addition(x, y, z=1)
        # subtraction
        if z == 1:
            subtraction(x, y, z=1)


def moderate(n):
    global score
    for i in range(n):
        x = random.randint(-10, 50)
        y = random.randint(-10, 50)
        z = random.randint(1, 4)
        # addition
        if z == 1:
            addition(x, y, z=5)
        # subtraction
        elif z == 2:
            subtraction(x, y, z=5)
        elif z == 3:
            # multiplication
            multiplication(x, y, z=5)
        else:
            # division
            division(x, y, z=5)


def hard(n):
    global score
    for i in range(n):
        x = random.randint(-30, 60)
        y = random.randint(-30, 60)
        z = random.randint(1, 2)
        if z == 1:
            # multiplication
            multiplication(x, y, z=10)
        else:
            # division
            division(x, y, z=10)


def main():
    while True:
        print('*' * 25)
        print('Enter 0 to quit')
        print('Enter 5 to show score')
        print('-' * 15)
        choice = int(input('Select Level\n1.easy\n2.Moderate\n3.Hard\n='))
        print()
        if choice == 0:
            break
        if choice == 5:
            print(score, " is your score")
            continue
        r = int(input('Enter no of rounds = '))
        if choice == 1:
            easy(r)
        elif choice == 2:
            moderate(r)
        elif choice == 3:
            hard(r)
        else:
            print('Wrong choice')
