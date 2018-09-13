x = 25
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
guess = (low + high)/2.0 #first guess

while abs(guess**2 - x) >= epsilon:
    print('low = ' + str(low) + ' High = ' + str(high) + ' quess = ' + str(guess))
    num_guesses += 1
    if guess**2 < x: #low guess
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0  # next guess
print('num_guesses = ' + str(num_guesses))
print(str(guess) + ' is close to the suare root of ' + str(x))