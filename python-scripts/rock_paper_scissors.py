#Language: Python
#Author: kaywinnet
#Play a game of Rock, Paper, Scissors

from random import randint

user_score = 0
computer_score = 0

for i in range(5):
    user = input('Choose Rock, Paper or Scissors!')
    user_input = user.lower()
    if user_input == 'rock':
        user_move = 1
        computer_move = randint(1,4)
        if computer_move == 1:
            print('The computer also chose Rock. It\'s a tie!')
            user_score = user_score + 1
            computer_score = computer_score + 1
        elif computer_move == 2:
            print('The computer chose Paper. You lost!')
            computer_score = computer_score + 1
        else:
            print('The computer chose Scissors. You won!')
            user_score = user_score + 1
    elif user_input == 'paper':
        user_move = 2
        computer_move = randint(1,4)
        if computer_move == 1:
            print('The computer chose Rock. You won!')
            user_score = user_score + 1
        elif computer_move == 2:
            print('The computer also chose Paper. It\'s a tie!')
            user_score = user_score + 1
            computer_score = computer_score + 1
        else:
            print('The computer chose Scissors. You lost!')
            computer_score = computer_score + 1
    elif user_input == 'scissors':
        user_move = 3
        computer_move = randint(1,4)
        if computer_move == 1:
            print('The computer chose Rock. You lost!')
            computer_score = computer_score + 1
        elif computer_move == 2:
            print('The computer chose Paper. You won!')
            user_score = user_score + 1
        else:
            print('The computer also chose Scissors. It\'s a tie!')
            user_score = user_score + 1
            computer_score = computer_score + 1
    else:
        print('You did not choose Rock, Paper or Scissors.')
        
if user_score == computer_score:
    print('Your score is', user_score, 'and the computer\'s score is', computer_score,'. It\'s a tie!')
elif user_score > computer_score:
    print('Your score is', user_score, 'and the computer\'s score is', computer_score,'. You won!')
else:
    print('Your score is', user_score, 'and the computer\'s score is', computer_score,'. You lost!')
