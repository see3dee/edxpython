x = float(input('please enter a value for x: '))
y = float(input('please enter a value for y: '))
if x == y:
    print('x is equal to y')
    if y!= 0:
        print('therefore, x / y is ', x/y)
elif x < y:
    print('x is smaller than y')
else:
    print('y is smaller than x')
print('we are done here!!')