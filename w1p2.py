let1 = 0
let2 = 1
let3 = 2
numbobs = 0
for index in range(len(s)-2):
    if s[let1]+s[let2]+s[let3] == 'bob':
        numbobs += 1
    let1 += 1
    let2 += 1
    let3 += 1
print('Number of times bob occurs is:', str(numbobs))



