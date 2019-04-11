#!python3

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    ## ------------BENCHMARKS------------- ##
    # SET OF COMBINATIONS:
    # 
    
    # ITERATIVE:
    # 
    ## ------------------------------------ ##
    # return contains_iter(text, pattern)
    return contains_set(text, pattern)
    # TODO: Implement contains here (iteratively and/or recursively)
    # 
    # SLOW!!
    # create a set of all combinations (in-order) of length pattern
    # if in set
    # 
    # FASTER!
    # linear serch text for first char of pattern in text
    # then check next letter and so on
    # until index more than text minus length of pattern
    # 
    # .

def contains_set(text, pattern):
    combinations = set()
    # create a set of all possible combinations
    for ind in range(0, len(text)+1):
        combinations.add(text[ind : ind+len(pattern)])

    if pattern in combinations:
        return True
    else:
        return False


def contains_iter(text, pattern, text_ind=0):

    def find_next(text_ind):
        """return the next index in text of the first char of pattern in text
        if the pattern is too long to fit in text after that index return False"""
        while text[text_ind] != pattern[0]:
            if text_ind < (len(text) - len(pattern)):
                text_ind += 1
            # pattern cant fit in text after index
            else:
                return False
        return text_ind

    for ind, letter in enumerate(pattern):
        temp_ind = text_ind + ind
        # not equal and not possible for further match based on length
        if text[temp_ind] != letter and temp_ind > (len(text) - len(pattern)):
            return False
        # not match so get next index of mathcing first letter in pattern
        elif text[temp_ind] != letter:
            text_ind = find_next(temp_ind)
            if text_ind == False:
                return False
    return True
    


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
