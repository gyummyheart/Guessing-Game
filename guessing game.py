import random

guessesTaken = 0

print('Hello! Pick a range of numbers to guess between. Please enter the low number.')
numberlow = int(input())
print('Now enter a high number!')
numberhigh = int(input())

number = random.randint(numberlow, numberhigh)
print('Let\'s get started')

while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
