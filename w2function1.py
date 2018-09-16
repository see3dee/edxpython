def f(x):
    x = x + 1
    print('in f(x): x = ', x)
    return x

def g(x):
    x = x + 10
    print('in g(x): x = ', x)
    return x
x = 3
z = f( x )
g = g( x )
print(x)
print(z)
print(g)