import random

# Hangman game is to guess a random number.
# User guess a number each time between 1 and 50.
# The random number is chosen by the computer.


def get_random_number():
    """
    The function is to get random number.
    """
    random_number = random.randint(0, 50)
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
            break
            

        elif user_choice.lower() == 'no':
            print('No worries! Until next time.')
            print()
            quit()

        else:
            print('Invalid data.')
            print("Please enter 'yes' or 'no' next time.")
            print()
            continue
            


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

            break


# get_user_name()

def validate_user_answer():
    """
    The function is to validate user's answer,
    to see if user enters a digit.
    """

    while True:
        # try:
        #     user_answer = input('Please guess a number between 0 and 50: ')

        # except ValueError():
        #     print('Invalid data. Please enter a number: ')
       

        if user_answer.isdigit():
            user_answer = int(user_answer)

        # elif user_answer <= 0:
        #     print('Please enter a number bigger than 0: ')

        else: 
            print('Please enter only numbers next time.')
            print()

# validate_user_answer()


            

def play_game():
    """
    The function is to play the game.
    User guess a number each time.
    User gets a hint after each guessing.

    """

    attempts = 0
    max_attempts = 10

    answer = random.randint(0, 50)
    user_answer = input('Please guess a number: ')

    while user_answer != answer:
        if user_answer > answer:
            print('Your number is too big. Please try again!')

        elif user_answer < answer:
            print('Your number is too small. Please try again!')



play_game()




    


# play_game()

def hangman_image():
    """
    The function is to print out the Hangman
    on each time user guesses a wrong letter.
    """


def main():
    """
    The function is to call all of the functions.
    """
    answer = get_random_number()
    ask_user_to_play_or_not()
    username = get_user_name()
    user_answer = validate_user_answer()

# main()