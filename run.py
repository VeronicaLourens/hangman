import random

# Hangman game is to guess a color.
# User makes a guess by guessing a letter each time.
# The color is chosen by the computer randomly.


# A list of colors

colors = [
    'aqua',
    'blue',
    'green',
    'yellow',
    'orange',
    'red',
    'white',
    'violet',
    'indigo',
    'brown',
    'black',
    'navy',
    'purple',
    'rose',
    'gray',
    'silver',
    'orchid',
    'golden'
]

def get_random_color():
    """
    The function is to get random color.
    """

    color = random.choice(colors)
    print(color)


def ask_user_to_play_or_not():
    """
    The function is to let user decide 
    if he/she plays the game or not.
    print out the messages base on user's answer.
    """

    while True:

        user_choice = input('Would you like to play Hangman game? ')
        print('\n')

        if user_choice == 'yes':
            print("Great! Let's go ahead and play.")
            print()

        elif user_choice == 'no':
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


def play_game():
    """
    The function is to play the game.
    User guess a color by enter a letter each time.

    """


def hangman_image():
    """
    The function is to print out the Hangman body parts
    on each time user guesses a wrong letter.
    """


def main():
    """
    The function is to call all of the functions.
    """
    get_random_color()
    ask_user_to_play_or_not()

main()