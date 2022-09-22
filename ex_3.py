"""
Write a function that returns a set of all characters appearing more
than a given number of times in a string.
Example of use:
# >>> more_than('mary had a little lamb', 3)
{'a', ' '}

"""


def more_then(sentence, n):
    freq = {}
    for character in sentence:
        if character not in freq:
            freq[character] = 0
        freq[character] += 1

    #result = set()
    #for k, v in freq.items(): # .item() allows us to iterate over keys and values at the same time
    #    if v > n:
    #        result.add(k)
    #return result
    return {k for k, v in freq.items() if v > n}

print(f"{more_then('mary had a little lamb', 3) = }")