x = int(input('enter an integer for which you would like the cube-root: '))
for guess in range(x + 1):
    if guess**3 == x:
        print(guess, 'is the cube root of ', x)
if guess == x:
    print(x, 'is not a perfect cube.')


