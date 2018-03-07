from random import *


def start():
    print('I am thinking of a number from 1-10. Can you find it? You have 5 tries.')
    rand = randint(1, 10)
    print(rand)
    counter = 0
    while True:
        guess = input("Guess what it is: ")
        if int(guess) == rand:
            counter += 1
            print(f"Congratulations! You have guessed it in {counter} tries!")
            play_again()
        elif int(guess) > rand:
            counter += 1
            check_counter(counter)
            print("Nope. It's lower than that. Try again.")
        elif int(guess) < rand:
            counter += 1
            check_counter(counter)
            print("Nope. It's higher than that. Try again.")
        elif not int(guess):
            print("Probably not int.")


def play_again():
    again = input("Do you want to play again? (y/n): ")
    if again == 'y':
        start()
    elif again == 'n':
        print("Bye!")
        exit()


def check_counter(c):
    if c >= 5:
        print("------------ You have used all your tries. ----------")
        play_again()


start()
