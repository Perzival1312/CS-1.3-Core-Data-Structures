#!python3

import sys

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
    return find(text, pattern)
    # return contains_set(text, pattern)
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


def find(text, pattern, text_ind=0):#, caller=None, indexes=[]):
    """Iterative implementation of the contains function"""

    # if caller == None:
    if sys._getframe().f_back.f_code.co_name == 'contains':
        empty = True
        dne = False
    elif sys._getframe().f_back.f_code.co_name == 'find_index':
        empty = 0
        dne = None
        # elif sys._getframe().f_back.f_code.co_name == 'find_all_indexes':
        #     caller = 1
        #     indexes = []
        #     empty = [x for x in range(0, len(text))]
        #     dne = indexes
        
    if pattern == '':
        return empty

    # elif caller == 1:
    #     print(text[text_ind:], pattern)

    def find_next(ind):
        """return the next index in text of the first char of pattern in text
        if the pattern is too long to fit in text after that index return False"""
        while text[ind] != pattern[0]:
            # pattern is still possible
            if ind < (len(text) - len(pattern)):
                ind += 1
            # pattern cant fit in text after index
            else:
                return len(text) + 1
        return ind

    pat_ind = 0
    while pat_ind < len(pattern):
        letter = pattern[pat_ind]

        temp_ind = text_ind + pat_ind

        # not match so get next index in text of mathcing first letter in pattern
        if text[temp_ind] != letter:
            text_ind = find_next(text_ind+1)
            pat_ind = 0
            if text_ind > len(text):
                return dne
            # else:
        pat_ind += 1
    # print('prev:', sys._getframe().f_back.f_code.co_name == 'contains')
    # print(sys._getframe().f_back.f_code.co_name)
    if sys._getframe().f_back.f_code.co_name == 'contains':
        return True
    elif sys._getframe().f_back.f_code.co_name == 'find_index':
        return text_ind   
    # else:
    # elif sys._getframe().f_back.f_code.co_name == 'find_all_indexes' or caller < (len(text)//len(pattern))+1:
    #     print(sys._getframe().f_back)
    #     # print(text_ind)
    #     indexes.append(text_ind)
    #     if text_ind < (len(text) - len(pattern)):
    #         # print(text[text_ind:], pattern)
    #         possible_next = find(text, pattern, text_ind, caller+1, indexes)
    #         print(possible_next, pattern)
    #         if isinstance(possible_next, int):
    #             indexes.append(possible_next)
    #     return indexes


def find_index(text, pattern, start=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    return find(text, pattern, start)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # return find(text, pattern)

    if pattern == '':
        return [x for x in range(0, len(text))]
    
    indexes = []
    possible_ind = find_index(text, pattern)

    # if isinstance(possible_ind, int):
    #     indexes.append(possible_ind)

    while isinstance(possible_ind, int):
        indexes.append(possible_ind)
        if possible_ind < (len(text) - len(pattern)) and (possible_ind+len(pattern)) <= len(text):
            try:
                possible_ind = find_index(text, pattern, possible_ind+1)
            except IndexError:
                possible_ind = None
        else:
            possible_ind = None

    return indexes


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
