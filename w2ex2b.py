x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print(guess, 'is the current guess')
        print('the value of x is',x)
        print(abs(guess**2 -x) >= epsilon)

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
