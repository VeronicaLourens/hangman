"""
Import modules needed for the project.
"""

# Import random module to get the random number.
import random

# Import colorama to color the text.
import colorama
from colorama import Fore, Style
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
        print('  Would you like to play around?')
        user_choice = input("  Please enter 'yes' or 'no': ")
        print('\n')

        if user_choice.lower() == 'yes':
            print(Fore.LIGHTYELLOW_EX + "  Great!")
            print(Fore.LIGHTYELLOW_EX + "  Let's go ahead and play!")
            print()
            return True

        elif user_choice.lower() == 'no':
            print()
            print(Fore.LIGHTGREEN_EX + '  Thank you for stopping by.')
            print()
            print('  Have a great day! Bye-bye!')
            print(Fore.LIGHTGREEN_EX + '==============================')
            print()
            quit()

        else:
            print()
            print(Fore.LIGHTRED_EX + '  Invalid entry.')
            print("  Please enter 'yes' or 'no'.")
            print(Fore.YELLOW + '===============================')
            print()

            continue


def get_user_name():
    """
    The function is to get user's name.
    Displays welcoming message to the user.
    """

    name = False

    while not name:

        user_name = input('  Please enter your name:  ')

        if user_name.isalpha():

            print()
            print(Fore.GREEN + '  Nice to meet you  ' + user_name + '!')
            print()
            break

        else:
            print()
            print(Fore.LIGHTRED_EX + '  Invalid entry.')
            print('  Name can only be alphabets.')
            print('===============================')
            print()
            continue

        return user_name


def play_game(user_name):
    """
    The function is to play the game.
    User guesses a number each time.
    User gets a hint after each guessing.
    Prints hangman on each wrong answer.
    """

    attempts = 0
    max_attempts = 7
    is_playing = False
    user_name = ''

    answer = random.randint(0, 50)
    while not is_playing and max_attempts > 0:

        print('  Please guess a number.')
        user_answer = input('  Between 0 and 50: ')

        if user_answer.isdigit():
            user_answer = int(user_answer)
            attempts += 1

            if user_answer > answer:
                print()
                print(Fore.RED + '  Your number is too big.')
                print(Fore.RED + '  Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))

            elif user_answer < answer:
                print()
                print(Fore.YELLOW + '  Your number is too small!')
                print(Fore.YELLOW + '  Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -= 1

                print(print_hangman(attempts))

            else:
                print()
                print(Fore.CYAN + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print()
                print(Fore.LIGHTRED_EX + '   CONGRATULATIONS!')
                print()
                print(Fore.LIGHTYELLOW_EX + '  You  WON  the  game!')
                print()
                print('  Great job! The answer is', answer, '.')
                print('  You guessed correctly in', attempts, 'attempts.')
                print()
                print(Fore.CYAN + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print()
                
                while True:
                    print()
                    print()
                    print('  Would you like to play again?')
                    play_again = input("  Please enter 'yes' or 'no':  ")

                    if play_again.lower() == 'yes':
                        print()
                        play_game(user_name)

                    elif play_again.lower() == 'no':
                        print()
                        print()
                        print(Fore.YELLOW + '  Thank you for playing!')
                        print()
                        print('  See you next time.')
                        print()
                        print(Fore.CYAN + '========================')
                        print()
                        quit()

                    else:
                        print()
                        print(Fore.LIGHTRED_EX + '  Invalid entry.')
                        print("  Please enter 'yes' or 'no'.")
                        print('===============================')
                        # ask_user_to_play_or_not()

                break
        
        elif not user_answer.isdigit():
            print()
            print(Fore.LIGHTRED_EX + '  Invalid entry.')
            print('  Please enter only digit numbers.')
            print('===================================')
            print()

        elif user_answer > 50:
            print()
            print(Fore.LIGHTRED_EX + '  Invalid entry.')
            print('  Please enter a number between 0 and 50.')
            print('==========================================')
            print()
  
        else:
            print()
            print(Fore.LIGHTRED_EX + '  Invalid entry.')
            print('  Please enter intergers between 0 and 50!')
            print('===============================')
            print()


def validate_user_answer():
    """
    "Validate user's answer.
    """

    user_answer = range(0, 50)

    while not user_answer:

        user_answer = int(user_answer)

        if user_answer < 0:
            print('Please enter a number bigger than 0.')

        elif user_answer > 50:
            print('Please enter a number smaller than 50.')

        else:
            play_game()

    
def print_hangman(attempts):
    """
    The function is to print out the Hangman
    on each time user guesses a wrong number.
    Prints one part of the body each time.
    """

    spacer = '========='
    
    if attempts == 0:
        print('\n*------*')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 1:
        print('\n*------*')
        print('   |   |')
        print('       |')
        print('       |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 2:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('       |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 3:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('   |   |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 4:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|   |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 5:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('       |')
        print('       |')
        return spacer

    elif attempts == 6:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  /    |')
        print('       |')
        return spacer

    elif attempts == 7:
        print('\n*------*')
        print('   |   |')
        print('   O   |')
        print('  /|\  |')
        print('  / \  |')
        print('       |')
        print('========')
        print()
        print(Fore.LIGHTCYAN_EX + '****** G a m e  O v e r! ******')
        print()
        print('      Ooopsie-daisy...    ')
        print(Fore.LIGHTRED_EX + '    You lost the game!')
        print(Fore.YELLOW + '  Please try again next time! ')
        print()
        print(Fore.LIGHTCYAN_EX + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()

        while True:

            print()
            print('   Would you like to play again?')
            play_again = input("   Please enter 'yes' or 'no':  ")
            print()
            print()
            if play_again.lower() == 'yes':
                play_game(user_name)

            elif play_again.lower() == 'no':
                print()
                print(Fore.LIGHTMAGENTA_EX + '  Thank you for playing!')
                print()
                print(Fore.LIGHTYELLOW_EX + '  See you next time!')
                print()
                quit()

            else:
                print()
                print(Fore.LIGHTRED_EX + '  Invalid entry.')
                print("  Please enter 'yes' or 'no'.")
                print(Fore.YELLOW + '===============================')
                print()


def main():
    """
    The function is to call all of the functions.
    """

    attempts = 7
    ask_user_to_play_or_not()
    user_name = get_user_name()
    play_game(user_name)
    validate_user_answer()
    print_hangman(attempts)


print()
print(Fore.LIGHTMAGENTA_EX + '************************************')
print()
print(Style.BRIGHT + '     WELCOME TO HANGMAN GAME!')
print()
print(Fore. LIGHTMAGENTA_EX + '************************************')
print('\n*-----*   Game Info:')
print('  |  |')
print(Fore.LIGHTYELLOW_EX + '  O  |  Follow the prompts.')
print(Fore.LIGHTRED_EX + ' /|\ |  Guess a number.')
print(Fore.LIGHTYELLOW_EX + ' / \ |  Maximum 7 attempts.')
print('     |')
print('======  Happy playing!')
print()
print()


main()
 