print('Please think of a number between 0 and 100!')
high = 100
low = 0
magic_num = int(high + low)/2
print('Is your secret number ' + str(magic_num) + '?')

response = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.')

while response == ('h' or 'l'):
    if response == ('h'):
        print('got here')