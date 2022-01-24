import random

tries_number = 0
user_number = 0
random_number = random.randint(1, 9)

while user_number != random_number:
    user_number = int(input('Guess the number from 1 to 9: '))
    tries_number += 1
    if user_number == random_number:
        print(f'You are right! The hidden number was {random_number}')
        break

    user_number = int(user_number)

    if user_number > random_number and user_number != random_number:
        print('You are too high')
    elif user_number < random_number and user_number != random_number:
        print('You are too low')

if tries_number == 1 and user_number == random_number:
    print(f'Congratulations, you have only {tries_number} trie!')
else:
    print(f'Congratulations, you have only {tries_number} tries!')


