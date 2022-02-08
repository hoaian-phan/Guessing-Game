"""A number-guessing game."""

import math
import random

#1 print greeting
print("Howdy, what's your name?")
#2 Ask user to input their name
name = input("(type in your name) ") 

print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")

#3
random_num = random.randint(1, 100)
# random.randint(0, 9)	dom(math.range(1,100))
# print(random_num)


k = 0
finish = False
while not finish:
    raw_guess = input("Type in your guess ")
    k += 1
    if raw_guess.isdigit() and int(raw_guess) < 101:
        guess = int(raw_guess)
        if guess == random_num:
            print(f"Congratulations, {name}, you found my number in {k} tries!")
            finish = True
        elif guess < random_num:
            print("\n Your guess is too low, try again \n")
        else:
            print("\n Your guess is too high, try again \n")

    else:
        print("Sorry this is not valid choice. Please use numbers from 1 to 100 only")
