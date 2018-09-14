high = 100
low = 0
guess = int((high + low)//2)
stillguessing = True
print('Please think of a number between 0 and 100!')

while stillguessing == True:
    print('Is your secret number ' + str(guess) + '?')
    response = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if response == ('h'):
        high = guess
        guess = int(high + low) // 2

    elif response == ('l'):
        low = guess
        guess = int(high + low) // 2

    elif response == ('c'):
        print('Game over. Your secret number was: ' + str(guess))
        stillguessing = False

    else:
        print('Sorry, I did not understand your input.')