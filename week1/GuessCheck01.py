x = int(input('Enter the integer that you would like to know cube-root for: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x), 'is not a perfect cube')
else:
    if x < 0:
        ans =  -ans
    print('The cube root of ' + str(x) + ' is ' + str(ans))

