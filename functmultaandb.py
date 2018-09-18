def mult_ab (a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_ab(1000, 1000))

