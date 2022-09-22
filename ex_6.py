def count_char(string: str, start: str = '<', end: str = '>'):
    """
    This function will count the number of characters between '< & >' symbols
    :param string: words in the sentence
    :param start: point started using '<'
    :param end: point started using '>'
    :return:
    """

    are_we_inside_brackets = False
    count = 0

    for letter in string:
        if letter == start:
            are_we_inside_brackets = True
        elif letter == end:
            are_we_inside_brackets = False
        elif are_we_inside_brackets:
            count += 1

    return count


print(count_char('Mart <had> a little lamp'))



