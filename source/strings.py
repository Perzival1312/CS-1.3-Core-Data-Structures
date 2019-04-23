#!python3

import sys

def _find(text, pattern, dne, text_ind=0):
    """Finds the first occurance of 'pattern' in 'text' after 'text_ind'\n
    'text' - String that is being searched\n
    'pattern' - String that is being searched for\n
    'dne' - value to return if 'pattern' is not found in 'text'\n
    'empty' - value to return if 'pattern' is an empty string\n
    'text_ind' - Integer index of text to start searching from"""
    # best case O(1) where length of pattern is 1 and its at the beginning of text
    # worst case O(n*m) where n is length of text and m pattern and text has
    # a repeating beginning segment of pattern

    assert isinstance(text_ind, int), "text_ind is not an int: {}".format(text_ind)

    def find_next(ind):
        """return the next index in text of the first char of pattern in text
        if the pattern is too long to fit in text after that index
        return an invalid index in text"""
        while ind < len(text) and text[ind] != pattern[0]:
            # pattern is still possible
            if ind < (len(text) - len(pattern)):
                ind += 1
            # pattern cant fit in text after index
            else:
                return len(text) + 1
        return ind

    pat_ind = 0
    while pat_ind < len(pattern):
        # make it easier to call specific char in pattern
        letter = pattern[pat_ind]
        # tentatively test next letters in pattern
        temp_ind = text_ind + pat_ind
        # not match so get next index in text of matching first
        # letter in pattern and restart the while loop.
        if text[temp_ind] != letter:
            text_ind = find_next(text_ind + 1)
            pat_ind = 0
            if text_ind >= len(text):
                return dne
        # iterate through while loop/pattern
        pat_ind += 1
    return text_ind


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    best O(1) worst O(n*m)"""
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    # default value
    dne = None

    result = _find(text, pattern, dne)
    # pattern exists in text
    if result is not None:
        return True
    else: # DNE
        return False


def find_index(text, pattern, start=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found. best O(1) worst O(n*m)"""
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)
    # default value
    dne = None
    return _find(text, pattern, dne, start)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found. always worst case O(n*m) """
    assert isinstance(text, str), "text is not a string: {}".format(text)
    assert isinstance(pattern, str), "pattern is not a string: {}".format(text)

    indexes = []
    # get first possible index
    possible_ind = find_index(text, pattern)
    # get all next indexes
    while isinstance(possible_ind, int):
        indexes.append(possible_ind)
        if possible_ind < (len(text) - len(pattern)) \
        and possible_ind + len(pattern) <= len(text):
            # get next
            possible_ind = find_index(text, pattern, possible_ind + 1)
        else:
            possible_ind = None
    # edge
    if pattern == "":
        return indexes[:-1]

    return indexes


def test_string_algorithms(text, pattern):
    # all O(n*m) where n is len(text) and m is len(pattern)
    found = contains(text, pattern)
    print("contains({!r}, {!r}) => {}".format(text, pattern, found))
    index = find_index(text, pattern)
    print("find_index({!r}, {!r}) => {}".format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print("find_all_indexes({!r}, {!r}) => {}".format(text, pattern, indexes))


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
        print("Usage: {} text pattern".format(script))
        print("Searches for occurrences of pattern in text")
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == "__main__":
    main()
