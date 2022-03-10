import random

# Hangman game is to guess a random number.
# User guess a number each time between 1 and 50.
# The random number is chosen by the computer.


def get_random_number():
    """
    The function is to get random number.
    """
    random_number = random.randint(1, 50)
    print(random_number)


def ask_user_to_play_or_not():
    """
    The function is to let user decide,
    if he/she plays the game or not.
    print out the messages base on user's answer.
    """

    while True:

        user_choice = input('Would you like to play Hangman game? ')
        print('\n')

        if user_choice.lower() == 'yes':
            print("Great! Let's go ahead and play.")
            print()
            

        elif user_choice.lower() == 'no':
            print('No worries! Until next time.')
            print()
            quit()

        else:
            print('Invalid data.')
            print("Please enter 'yes' or 'no' next time.")
            print()


def get_user_name():
    """
    The function is to get user's name.
    Display welcoming message to the user.
    """

    while True:

        user_name = input('Please enter your name: \n')

        if user_name.isalpha():

            print()
            print('Nice to meet you  ' + user_name + '!')
            


get_user_name()
            

def play_game():
    """
    The function is to play the game.
    User guess a number each time.
    User gets a hint after each guessing.

    """


def hangman_image():
    """
    The function is to print out the Hangman
    on each time user guesses a wrong letter.
    """


def main():
    """
    The function is to call all of the functions.
    """
    get_random_number()
    ask_user_to_play_or_not()
    get_user_name()

# main()