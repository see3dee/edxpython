x = int(input('please enter a value for x: '))
y = int(input('please enter a value for y: '))
z = int(input('please enter a value for z: '))

if x < y and x < z:
    print('x is the smallest value')
elif y < z:
    print ('y is the smallest')
else:
    print('z is the smallest')