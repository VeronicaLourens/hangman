import random

# Hangman game is to guess a random number.
# User guess a number each time between 0 and 50.
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
    """

    attempts = 0
    max_attempts = 6
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
                print()

                max_attempts -=1
                print(hangman_image(attempts))
                continue

            elif user_answer < answer:
                print()
                print('Your number is too small. Please try again!')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()

                max_attempts -=1
                print(hangman_image(attempts))

            else:
                print()
                print('You won! The answer is', answer, '.')
                print('You guessed correctly in', attempts, 'attempts.')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                break

        else:
            print()
            print('Invalid data. Please enter a number!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()


    print(hangman_image(attempts))



def print_hangman(attempts):
    """
    The function is to print out the Hangman
    on each time user guesses a wrong number.
    """

    lives = [
        """
        |------->
        |     |  
        |
        |
        |
        |
        |
        ~~~~~~~~~~~
        """, 
        """
        |------->
        |     |
        |     O
        |
        |
        |
        |
        ~~~~~~~~~~~
        """,
        """
        |------->
        |     |
        |     O
        |     |
        |
        |
        |
        ~~~~~~~~~~~
        """,
        """
        |------->
        |     |
        |     O
        |     |\
        |
        |
        |
        ~~~~~~~~~~~
        """,
        """
        |------->
        |     |
        |     O
        |    /|\
        |
        |
        |
        ~~~~~~~~~~~
        """,
        """
        |------->
        |     |
        |     O
        |    /|\
        |      \
        |
        |
        ~~~~~~~~~~~
        """,
        """
        |------->
        |     |
        |     O
        |    /|\
        |    / \
        |
        |
        ~~~~~~~~~~~
        """
    ]

    return lives[attempts]

    
        


def main():
    """
    The function is to call all of the functions.
    """
    get_random_number()
    ask_user_to_play_or_not()
    get_user_name()
    play_game()
    print_hangman(attempts)

main()