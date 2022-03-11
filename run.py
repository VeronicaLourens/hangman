import random

# Hangman game is to guess a random number.
# User guess a number each time between 0 and 50.
# The random number is chosen by the computer.

# def get_random_number():
#     """
#     The function is to get random number.
#     """
#     random_number = random.randint(0, 50)
#     return random_number


def ask_user_to_play_or_not():
    """
    The function is to let user decide,
    if he/she plays the game or not.
    print out the messages base on user's answer.
    """

    while True:

        user_choice = input('Would you like to play Hangman game? ')
        # print('\n')

        if user_choice.lower() == 'yes':
            print("Great! Let's go ahead and play.")
            print()
           # break
            return True
            

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

def play_game():
    """
    The function is to play the game.
    User guess a number each time.
    User gets a hint after each guessing.
    Print hangman on each wrong answer.
    """

    attempts = 0
    max_attempts = 7
    isPlaying = False

    answer = random.randint(0, 50)
   
    while not isPlaying and max_attempts > 0:
        attempts +=1
        user_answer = input('Please guess a number between 0 and 50: ')

        if user_answer.isdigit():
            user_answer = int(user_answer)

            if user_answer > answer:
                print()
                print('Your number is too big. Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                # print()

                max_attempts -=1
                print(print_hangman(attempts))
                # print(hangman)
                continue

            elif user_answer < answer:
                print()
                print('Your number is too small. Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                # print()

                max_attempts -=1
                print(print_hangman(attempts))
                # print(hangman)

            else:
                print()
                print('Congratulations! You WON the game!')
                print('The answer is', answer, '.')
                print('You guessed correctly in', attempts, 'attempts.')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                # print()
                continue
                
        else:
            print()
            print('Invalid data. Please enter a number!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()

# play_game()


def print_hangman(attempts):
    """
    The function is to print out the Hangman
    on each time user guesses a wrong number.
    Prints one part of the body each time.
    """

    # attempts = 7

    if(attempts == 0):
        print('\n*----*')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 1):
        print('\n*----*')
        print(' |   |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 2):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print('     |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 3):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 4):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print('/|   |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 5):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('     |')
        print('     |')
        print('   ====')

    elif(attempts == 6):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/    |')
        print('     |')
        print('   ====')

    elif(attempts == 7):
        print('\n*----*')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |')
        print('   ====')
        print('Ooopsie...Game over!')
        print('You lost the game!')
        print('Please try again next time!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       # break

    # return print_hangman(attempts)

    
# print_hangman(attempts)

def restart_game():
    """
    The function is to restart the game.
    """
    game_over = False

    while True:
        play_again = input('Would you like to play again?')

        if play_again.lower() == 'yes':
            return True

        else:
            return False


def main():
    """
    The function is to call all of the functions.
    """

    attempts = 7
    # get_random_number()
    ask_user_to_play_or_not()
    get_user_name()
    # game = play_game()
    play_game()
    print_hangman(attempts)
    # hangman = print_hangman(attempts)
    restart_game()



# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('Welcome to the Hangman Game.')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

main()