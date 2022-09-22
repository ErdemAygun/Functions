def average(*numbers):
    if len(numbers) == 0:
        return None
    #or
    if not numbers:
        return None

    return sum(numbers) / len(numbers)

print((average(10, 20, 30)))
average(10, 20, 30)