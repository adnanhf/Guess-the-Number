import random as rnd

#Created 2nd
logo = '''
   _____                          _______  _             _   _                    _                 
  / ____|                        |__   __|| |           | \ | |                  | |                
 | |  __  _   _   ___  ___  ___     | |   | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ 
 | | |_ || | | | / _ \/ __|/ __|    | |   | '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
 | |__| || |_| ||  __/\__ \\__ \    | |   | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   
  \_____| \__,_| \___||___/|___/    |_|   |_| |_| \___| |_| \_| \__,_||_| |_| |_||_.__/  \___||_|   

'''

#Created 3rd
def generate_answer():
    return rnd.randint(1, 100)

#Created 4th
def guessing_chance(difficulty):
    if difficulty.lower() == 'easy':
        return 10
    elif difficulty.lower() == 'hard':
        return 5

#Created 5th
def start_guessing(attempts,the_answer):
    while not attempts == 0:
        print(f'You have {attempts} attempt(s) remaining to guess the number.')
        player_guess = int(input('Make a guess: '))
        if player_guess > the_answer:
            print('Too high.\nGuess again.')
            attempts -= 1
        elif player_guess < the_answer:
            print('Too low.\nGuess again.')
            attempts -= 1
        elif player_guess == the_answer:
            print(f'You got it! The answer was {the_answer}.')
            break
    else:
        print('You\'ve run out of guesses, you lose.')

#Created 1st
def play_game():
    print (logo)

    #Welcoming player
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100')

    #Generate the answer
    answer = generate_answer()
    #print(f'Pssst, the correct answer is {answer}')

    #Offer to choose the difficulty
    level = input('Choose a difficulty. Type \'easy\' or \'hard\':')
    while level != 'easy' and level != 'hard':
        level = input('Choose a difficulty. Type \'easy\' or \'hard\':')
    else:
        chance = guessing_chance(level)

    #Start guessing
    start_guessing(chance,answer)

play_game()
