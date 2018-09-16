num = 19
if num < 0:
    isNeg=True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = ''
while num > 0:
    print(result)
    result = str(num%2) + result
    num = num//2
    print(result)
if isNeg:
    result = '-'+ result


