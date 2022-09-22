#Fibonacci

#fib(0) = 0
#fib(1) = 1
#fib(n) = fib(n - 1) + fib(n - 2)

"""
def fib(x):
    if x == 0 or x == 1:
        return x
    return fib(x - 1) + fib(x - 2)

print(fib(11))
"""


# write the above fuction without recursion
# hint: start with a list [0,1] and keep adding 2 last elements
# 0  1  2  3 ........n
#[0, 1, 2, 3, ....., fib(n)]
#while len(list) < n + 1


def fib(n):
    n = set()
    if n == 0 or n == 1:
        return n
    else:
        for i in n:

