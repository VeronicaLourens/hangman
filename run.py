"""
Import random module to get the random number.
"""

import random

# Hangman game is to guess a random number.
# User guesses a number each time between 0 and 50.
# The random number is chosen by the computer.


def ask_user_to_play_or_not():
    """
    The function is to let user decide to play or not.
    Prints out the messages base on user's answer.
    """

    while True:

        print()
        print('     Would you like to play Hangman game?')
        user_choice = input("     Please enter 'yes' or 'no': ")
        print('\n')

        if user_choice.lower() == 'yes':
            print("     Great! Let's go ahead and play.")
            print()
            return True

        elif user_choice.lower() == 'no':
            print()
            print('     No worries! Until next time.')
            print('=====================================')
            print()
            quit()

        else:
            print()
            print('     Invalid data.')
            print("     Please enter 'yes' or 'no' next time.")
            print('==============================================')
            print()

            continue         


def get_user_name():
    """
    The function is to get user's name.
    Displays welcoming message to the user.
    """

    while True:

        user_name = input('     Please enter your name: \n')

        if user_name.isalpha():

            print()
            print('     ***** Nice to meet you  ' + user_name + '! *****')

            break


def play_game():
    """
    The function is to play the game.
    User guesses a number each time.
    User gets a hint after each guessing.
    Prints hangman on each wrong answer.
    """

    attempts = 0
    max_attempts = 7
    is_playing = False

    answer = random.randint(0, 50)
   
    while not is_playing and max_attempts > 0:

        attempts += 1
        user_answer = input('     Please guess a number between 0 and 50: ')

        if user_answer.isdigit():
            user_answer = int(user_answer)

            if user_answer > answer:
                print()
                print('     Your number is too big. Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))
                continue

            elif user_answer < answer:
                print()
                print('     Your number is too small. Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))

            else:
                print()
                print('************* Congratulations! *************')
                print()
                print('            You  WON  the  game!     ')
                print()
                print('        Great job! The answer is', answer, '.')
                print('     You guessed correctly in', attempts, 'attempts.')
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print()

                while True:
                    print('     Would you like to play again?')
                    print()
                    play_again = input("     Please enter 'yes' or 'no': \n")

                    if play_again.lower() == 'yes':
                        print()
                        play_game()

                    elif play_again.lower() == 'no':
                        print()
                        print('***** Thank you for playing! *****')
                        print('        See you next time.')
                        print('==================================')
                        quit()

                break             
        else:
            print()
            print('     Invalid data. Please enter a number!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()


def print_hangman(attempts):
    """
    The function is to print out the Hangman
    on each time user guesses a wrong number.
    Prints one part of the body each time.
    """

    if attempts == 0:
        print('  \n*----*')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 1:
        print('  \n*----*')
        print('   |   |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 2:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('       |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 3:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('   |   |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 4:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('  /|   |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 5:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('       |')
        print('       |')
        print('     ====')

    elif attempts == 6:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  /    |')
        print('       |')
        print('     ====')

    elif attempts == 7:
        print('  \n*----*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  / \  |')
        print('       |')
        print('     ====')
        print()
        print('********* Game over! *********')
        print()
        print('        Ooopsie-daisy...    ')
        print('      You lost the game!')
        print('    Please try again next time! ')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()

        while True:
            play_again = input('     Would you like to play again? \n')

            if play_again.lower() == 'yes':
                play_game()

            elif play_again.lower() == 'no':
                print()
                print('****** Thank you for playing! ******')
                print()
                print('******** See you next time. ********')
                quit()


def main():
    """
    The function is to call all of the functions.
    """

    attempts = 7
    ask_user_to_play_or_not()
    get_user_name()
    play_game()
    print_hangman(attempts)
   
print()
print()
print('*******************************************')
print()
print('          Welcome to Hangman Game!         ')
print()
print('*******************************************')


main()
