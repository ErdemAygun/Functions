def hello():
    print("hello")

print("asgas")
hello()
hello()
print("qwer")

def hello_name(name):
    print(f"Hello, {name}")

hello_name("Erdem")

def double(x):
    return 2 * x

x = double(10)
print((f"{x = }"))
print(f"{double(double(x)) = }")
print(f"{double('asdf') = }")

def two_arguments(a, b):
    print((f"{a = }"))
    print((f"{b = }"))

two_arguments(5, 10)

# How to leave comments in functions
# type hinting
def multiply(a: int | float, b: int | float) -> int | float:
    """ Multiplies two numbers.

    This function uses standard multiply operator to multipy two arguments and returns the result of multiplication.


    :param a: first number
    :param b: second number
    :return: multiplication result
    """
    return a * b

print(multiply(2, 3))
print(multiply(1.4, 2.5))

# arguments with default value

def packer(string, prefix, suffix):
    return prefix + string + suffix

print(packer('Erdem', '>>', '<<'))

def hello(string: str, prefix: str ='>>', suffix: str ='<<') -> str:
    return prefix + string + suffix


# positional arguments
print(hello('Erdem'))
print(hello('Erdem', '..'))
print(hello('Erdem', '..', '!!'))
print(hello('Erdem', '>>', '##'))

# named arguments
print(hello(string='Erdem'))
print(hello(string='Erdem', prefix='..'))
print(hello(string='Erdem', prefix='..', suffix='!!'))

# for named arguments the order of the arguments doesn't matter
print(hello(prefix='..', string='Erdem', suffix='!!'))

# we can use positional and named arguments together
# positional arguments first and then named arguments
print(hello('Erdem', suffix='%%'))

print('-' * 60)
print('Erdem', 'Erdem', 123, True, None)
print('Erdem', 'Erdem', 123, True, None, sep='|')

# How to pass multiple arguments to a function?
# *args - catches all positional arguments into a tuple
# **kwargs - catches all named arguments into a dictionary

def counter(*args, **kwargs):
    print(args)
    print(kwargs)
    print('--')

counter(1)
counter(1, 2, 3)
counter(1, 2, 3, 'Tom', True, False, None)
counter(1, 2, 3, first_name='Tom', last_name='Doe', age=10)

# one-line if

person = {
    'first_name': 'Piotr',
    'last_name': 'GG',
}

if 'id' in person:
    has_id = True
else:
    has_id = False

print(has_id)

has_id = True if 'id' in person else False

print(has_id)

#############
print('-' * 60)

# falsy and truthy values

my_variable = '' # False
my_variable = 'Ala'
my_variable = -1
my_variable = 0


print(bool(my_variable))

# and
# or

# lazy condition avaliation

number = 50

new_number = number and 10
print(new_number)


number = 50

new_number = number or 10
print(new_number)

"""
# Name / variables scopes in python

- built-in scope
    -global (or module) scope
        -enclosing (or non local) scope
            -local (or function) scope
            
"""

print('-' * 60)

first_name = 'Erdem'

def test_function():
    print(first_name)

test_function()

print('-' * 60)

a = 1

def outer():
    a = 100
    print(a)

    def inner():
        print(f'inner a={a}')

    inner()

print(f'global a={a}')
outer()
print(f'global a={a}')

########################

# Lambda functions

print('-' * 60)

def square(x):
    return x ** 2

print(square(3))

square_lambda = lambda x: x ** 2

print(square_lambda(3))

my_fun = square_lambda

print(my_fun(4))


def adder(a, b, c):
    return a + b + c

print(adder(10, 20, 30))

adder_lambda = lambda a, b, c: a + b + c
print(adder_lambda(10, 20, 30))


def apply_operation_on_list(data_list: list, operation) -> list:
    result = []

    for element in data_list:
        result.append((operation(element)))

    return result

print(apply_operation_on_list([100, 200, 300], lambda x: x/10))

# MAP, mapping

result = map(lambda number: number/5, [100, 200, 300])
# map return an iterator
print(result)

for element in result:
    print(element)

print(list(map(lambda number: number/5, [100, 200, 300])))
print(tuple(map(lambda number: number/5, [100, 200, 300])))
print(set(map(lambda number: number/5, [100, 200, 300])))


# FILTER
print(list(filter(lambda number: number > 0, [10, -8, 23, -123, 88])))

# REDUCE
from functools import reduce

numbers = [-10, 4, 1, 4, 5, 10, 11]

result = reduce(lambda a, b: a + b, numbers)
print(result)

#any
names = ['Erdem', 'Piotr', None]
print(any(names))

names2 = [None, False, '', [], 0]
print(any(names2))

#all  - all boolean should be True
names = ['Erdem', '', None]
print(all(names))

# zip
first_names = ['Piotr', 'Tom', 'John']
last_names = ['GG', 'Nowak', 'Doe']

people = list(zip(first_names, last_names))
print(people)

"""
Sorting
- sort a list using build-in method of the list
-sorted() - gets an iterable as an argument and returns soreted data
"""

numbers = [ 1023, 5, -1, 123, -80]
print(numbers)
numbers.sort() # will sort numbers list in-place
numbers.sort(reverse=True)
print(numbers)

my_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(my_list)
my_list.sort()
print(my_list)

my_list.sort(key=lambda element: element[1])
print(my_list)

my_set = {90, 123, -10, 3, -123}
print(my_set)

sorted_elements_from_set = sorted(my_set) # returns list, not set
print(sorted_elements_from_set)
