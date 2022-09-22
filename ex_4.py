"""
def factorial(x):
    number = 1
    for i in range(1, x + 1):
        number = number * i
    return number

print(factorial(5))

"""
# recursive version
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
