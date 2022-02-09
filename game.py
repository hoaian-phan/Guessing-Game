"""A number-guessing game."""

import math
import random

#1 print greeting
print("Howdy, what's your name?")
#2 Ask user to input their name
name = input("(type in your name) ")

def is_valid_input(num):
    
def render_game():
    """
    render game you get 10 tries
    """
    random_num = random.randint(1, 100)
    print(random_num)
    count = 0
    finish = False
    max_tries = 10
    start_input = input("Pick a starting number: ")
    end_input = input("Pick an ending number: ")
    while not finish and count < max_tries:
        raw_guess = input("Type in your guess ")
        count += 1
        if raw_guess.isdigit() and int(raw_guess) < 100:
            guess = int(raw_guess)
            if guess == random_num:
                print(f"Congratulations, {name}, you found my number in {count} tries!")
                finish = True
            elif guess < random_num:
                print(f"\n Your guess is too low, try again. You have {max_tries - count} tries \n")
            else:
                print(f"\n Your guess is too high, try again You have {max_tries - count} tries \n")
        else:
            print(f"Sorry this is not valid choice. Please use numbers from 1 to 100 only. You have {max_tries - count} tries. ")
            
    return count



# new_round = input("Do you want to play a game? ").lower()
score_list = []
done_playing = False
while not done_playing:
    print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")
    score_list.append(render_game())
    new_round = input("Do you want to play again? ").lower()
    if new_round == 'yes':
        done_playing = False
    elif new_round == 'no':
        done_playing = True
        break
    else:
        print("please answer with yes or no")
        new_round = input("Do you want to play again? ").lower()

best_score = min(score_list)
print(f"Thanks {name}, maybe next time. Your best score was {best_score}.")




#3

# random.randint(0, 9)	dom(math.range(1,100))
# print(random_num)

