x = int(input('enter an integer for which you would like the cube-root: '))
for guess in range(abs(x) + 1):
    if guess **3 >= abs(x):
        break
if guess**3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        guess = -guess
    print(guess, 'is the cube root of ' , x )






