def get_user_guess():
    while True:
        try:
            guess=int(input("enter your gues (1-100):"))
            if 1<=guess <=100:
                return guess 
            else:
                print("please enter numbar between 1 and 100.")
        except ValueError:
            print("invalid input !Please enter a number.")

import random
def generate_random_number():
    return random . randintn(1-100)

def play_game():
    print("Welcome to the Number Guessing Game!")
    random_number = generate_random_number()
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("too high! try again.")
        else:
            print("congratulations! you guassed the number in {attempts}atempts.")
            break

