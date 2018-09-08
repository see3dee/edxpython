# n^2 = n+n+n+n+n+n.....n times
# ex. 3^2 = 3*3 = 3+3+3 = 9

n = 1000000
ans = 0
itersleft = n
while (itersleft > 0):
    ans = ans + n
    itersleft = itersleft - 1
print( str(n) + ' squared is equal to ' + str(ans))


