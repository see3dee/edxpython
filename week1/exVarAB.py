int_type = 1
str_type = 'string'

if type(varA)==type(varB) and type(varA)==type(int_type):
    if varA > varB:
        print('bigger')
    if varA == varB:
        print('equal')
    if varA < varB:
        print(('smaller'))
elif type(varA)==type(str_type):
    print('string involved')
elif type(varB) == type(str_type):
    print('string involved')














