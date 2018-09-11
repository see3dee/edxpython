x = int(input('please iput a value to see if it is divisible by 2 and/or 3: '))
if x%2 == 0:
    if x%3 == 0:
        print('That value is divisible by both 2 and 3!')
    else:
        print('That value is only divisible by 2')
elif x%3 == 0:
    print('That value is only divisible by 3')
