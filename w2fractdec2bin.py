
x = float(input('Enter a decimal between 0 ans 1: '))

p = 0
while (x*(2**p))%1 != 0:
    print('When p = ' + str(p) + ' The remainder is ' + str(x*(2**p) - int(x*(2**p))))
    p += 1
    print('p = ' + str(p))

num = int(x*(2**p))

if num < 0:
    isNeg=True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = ''
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p-len(result)):
    result = '0' + result
result = '.' + result

if isNeg:
    result = '-'+ result
print('The binary representation of the decimal ' + str(x) + ' is ' + result)
