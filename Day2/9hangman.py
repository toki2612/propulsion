from random import *


# game starts
def start():
    print("To quit the game simply type 'quit'.")
    print("You only have 7 tries for this game.")
    file = open("words_list.txt", "r")
    word = choose_word(file)

    # if there are more than 7 unique letters in a word
    if len(set(word)) > 7:
        print("HAHAHAHA, you'll never win!")

    print("\nWord is: " + word + " with length " + str(len(word)))
    user_guesses = []  # arr to store all user guess letters
    correct_guesses = []
    counter = 0  # max 7
    print('_ ' * len(word))

    while True:
        guess = input(f"\nYou have {7 - counter}/7 tries left.\n\nWrite your letter: ")

        if guess == 'quit':
            exit()

        if guess in user_guesses:
            print("You have already used this letter.")
        else:
            user_guesses.append(guess)
            print("You tried ", end="")
            print(user_guesses)

        if guess not in word:
            counter += 1

        for w in word:
            if w == guess:
                correct_guesses.append(guess)

        for w in word:
            if w in correct_guesses:
                print(w, end=' ')
            else:
                print("_", end=" ")

        check_counter(counter)

        # check if win
        if set(word) == set(correct_guesses):
            print("\n********** You win! *********\n")
            play_again()

# check if counter reached 7
def check_counter(c):
    if c >= 7:
        print("------------ You have used all your tries. ----------")
        play_again()


# choose a random word from the file
def choose_word(filename):
    # calculating the length of file
    words_list = []
    for i, w in enumerate(filename):
        words_list.append(w)

    return choice(words_list)[:-1]


def play_again():
    again = input("Do you want to play again? (y/n): ")
    if again == 'y':
        start()
    elif again == 'n':
        print("Bye!")
        exit()


start()
