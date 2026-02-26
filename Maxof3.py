def max_of_three(a, b, c):
    if a >= b and a >= c:
        print("max", a)
    elif b >= a and b >= c:
        print("max", b)
    else:
        print("max", c)

# Sample input
x = 12
y = 12
z = 8

max_of_three(x, y, z)

