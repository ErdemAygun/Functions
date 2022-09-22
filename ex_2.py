# Prime - a number, other than 1, that us divisible only by 1 and itself
# 7 prime
# 16 not prime
# 2 prime - only prime notmer which is even
# 3 prime
# 1 not prime (special case)
# 23 prime

#is_prime(x) returns True if x is prime and False otherwise

# pass empty instruction


def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

print(is_prime(11))
print(is_prime(13))
print(is_prime(100000000007))

