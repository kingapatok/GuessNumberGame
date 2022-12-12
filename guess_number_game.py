import random

print('-----------------------------------')
print(' Guess That Number Game ')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Guess a number game between 0 and 100: ')
    guess = int(guess_text)
    if the_number == guess:
        print("Yes! You've got it {}. The number was {}!".format(name, the_number))
    elif the_number < guess:
        print('Sorry {1}, but {0} is HIGHER than the number'.format(guess, name))
    else:
        print('Sorry {1}, but {0} is LOWER than the number'.format(guess, name))
print('Congrats!')

