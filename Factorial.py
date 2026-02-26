n = int(input("Enter a number: "))

if n < 0:
    print("Factorial not defined")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial =", factorial)
