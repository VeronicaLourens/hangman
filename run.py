"""
Import modules needed for the project.
"""

# Import random module to get the random number.
import random

# Import colorama to color the text.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
        print('   Would you like to play around?')
        user_choice = input("   Please enter 'yes' or 'no': ")
        print('\n')

        if user_choice.lower() == 'yes':
            print(Fore.LIGHTYELLOW_EX + "   Great! Let's go ahead and play.")
            print()
            return True

        elif user_choice.lower() == 'no':
            print()
            print('   No worries! Until next time.')
            print(Fore.LIGHTGREEN_EX + '====================================')
            print()
            quit()

        else:
            print()
            print(Fore.LIGHTBLUE_EX + '     Invalid data.')
            print("     Please enter 'yes' or 'no' next time.")
            print(Fore.LIGHTYELLOW_EX + '====================================')
            print()

            continue         


def get_user_name():
    """
    The function is to get user's name.
    Displays welcoming message to the user.
    """

    while True:

        user_name = input('   Please enter your name:  ')

        if user_name.isalpha():

            print()
            print(Fore.GREEN + '   Nice to meet you  ' + user_name + '!')
            print()

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
        user_answer = input('   Please guess a number between 0 and 50: ')

        if user_answer.isdigit():
            user_answer = int(user_answer)

            if user_answer > answer:
                print()
                print(Fore.LIGHTRED_EX + 'Your number is too big. Try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))
                continue

            elif user_answer < answer:
                print()
                print(Fore.YELLOW + 'Your number is too small. Try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))

            else:
                print()
                print(Back.LIGHTCYAN_EX + '       Congratulations!       ')
                print()
                print(Fore.LIGHTYELLOW_EX + '            You  WON  the  game!')
                print()
                print('        Great job! The answer is', answer, '.')
                print('     You guessed correctly in', attempts, 'attempts.')
                print()
                print(Fore.CYAN + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print()

                while True:
                    print()
                    print()
                    print('     Would you like to play again?') 
                    play_again = input("     Please enter 'yes' or 'no':  ")

                    if play_again.lower() == 'yes':
                        print()
                        play_game()

                    elif play_again.lower() == 'no':
                        print()
                        print()
                        print(Fore.YELLOW + '          Thank you for playing!')
                        print()
                        print('            See you next time.')
                        print()
                        print(Fore.CYAN + '=================================')
                        print()
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
        print('\n*------*')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('=========')

    elif attempts == 1:
        print('\n*------*')
        print('   |   |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('========')

    elif attempts == 2:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('       |')
        print('       |')
        print('       |')
        print('========')

    elif attempts == 3:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('   |   |')
        print('       |')
        print('       |')
        print('========')

    elif attempts == 4:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|   |')
        print('       |')
        print('       |')
        print('========')

    elif attempts == 5:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('       |')
        print('       |')
        print('========')

    elif attempts == 6:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  /    |')
        print('       |')
        print('========')

    elif attempts == 7:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  / \  |')
        print('       |')
        print('========')
        print()
        print(Fore.LIGHTCYAN_EX + '******** G a m e  O v e r! ********')
        print()
        print('        Ooopsie-daisy...    ')
        print(Fore.LIGHTRED_EX + '      You lost the game!')
        print(Fore.YELLOW + '    Please try again next time! ')
        print()
        print(Fore.LIGHTCYAN_EX + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()

        while True:

            print()
            print('    Would you like to play again?')
            play_again = input("    Please enter 'yes' or 'no':  ")         
            if play_again.lower() == 'yes':
                play_game()

            elif play_again.lower() == 'no':
                print()
                print(Fore.LIGHTMAGENTA_EX + '      Thank you for playing!')
                print()
                print(Fore.LIGHTYELLOW_EX + '         See you next time!')
                print()
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
print(Fore.LIGHTBLUE_EX + '*******************************************')
print()
print(Style.BRIGHT + '          Welcome to Hangman Game!         ')
print()
print(Fore. LIGHTBLUE_EX + '*******************************************')


main()
