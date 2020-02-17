#!python3

## ------------BENCHMARKS------------- ##
# ITERATIVE:
# 11.4 ms ± 141 µs per loop (mean ± std. dev. of 100 runs, 1000 loops each)

# RECURSIVE:
# 11.4 ms ± 318 µs per loop (mean ± std. dev. of 100 runs, 1000 loops each)

# ONE-LINER <-- DO NOT DO THIS STUPID SHIT!!
# 11.7 ms ± 1.06 ms per loop (mean ± std. dev. of 100 runs, 1000 loops each)
## ------------------------------------ ##

## ------------------------------------ ##
# http://norvig.com/pal21txt.html
## ------------------------------------ ##

## ------------------------------------ ##
# http://code.activestate.com/recipes/474088/
## ------------------------------------ ##
# this is a black box
# TODO: gain understanding
class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.
    
    This function fails if the decorated
    function recurses in a non-tail context.
    """

    def func(*args, **kwargs):
        # get frame object <-- wtf IS that???
        f = sys._getframe()
        # if prev exists and prev,prev exists and what is code?
        # basically if stack call length > 2 and f.f_code then repeats
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            # vs while True??
            while 1:
                try:
                    # What is all this after here tho??
                    return g(
                        *args, **kwargs
                    )  # <-- something to do with the fact it is a decorator?
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


## ------------------------------------ ##
# http://code.activestate.com/recipes/474088/
## ------------------------------------ ##

import string, sys

LETTERS = frozenset(string.ascii_letters)


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing.
    text - type String."""

    assert isinstance(text, str), "input is not a string: {}".format(text)

    # TODO: Change these to in the function instead of pre-processing
    text = text.lower()
    if not text:
        return True
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_one_liner(text)


def is_palindrome_iterative(text):
    # 11.4 ms ± 141 µs per loop (mean ± std. dev. of 100 runs, 1000 loops each)
    # initialize indexes of letters in text to compare
    left = 0
    right = len(text) - 1
    # Check each letter only once
    for _ in range(0, (len(text) // 2) + 1):
        # ignore everything but letters
        while text[left] not in LETTERS and left <= right:
            left += 1
        while text[right] not in LETTERS and left <= right:
            right -= 1
        # not palindromic
        if text[left] != text[right]:
            return False
        # increment and decrement index for next letters to compare
        left += 1
        right -= 1
    # PALINDROMIC!!
    return True


# DONT DO THIS SHIT ITS STUPID LMAO
def is_palindrome_one_liner(text):
    # 11.7 ms ± 1.06 ms per loop (mean ± std. dev. of 100 runs, 1000 loops each)
    # removes whitespace --> change to all lowercase --> remove all punctuation --> compare to reversed version
    return "".join(text.split(" ")).lower().translate(
        str.maketrans({key: None for key in string.punctuation})
    ) == "".join(text[::-1].split(" ")).lower().translate(
        str.maketrans({key: None for key in string.punctuation})
    )


@tail_call_optimized
def is_palindrome_recursive(text, left=0, right=None):
    # 11.4 ms ± 318 µs per loop (mean ± std. dev. of 100 runs, 1000 loops each)
    # initialize right on first run
    if right is None:
        right = len(text) - 1
    # conditional for recursive call
    if left <= right:
        # ignore everything but letters
        while text[left] not in LETTERS:
            left += 1
        while text[right] not in LETTERS:
            right -= 1
        # not palindromic
        if text[left] != text[right]:
            return False
        # increment and decrement index for next letters to compare
        left += 1
        right -= 1
        # Recursive call
        return is_palindrome_recursive(text, left, right)

    # PALINDROMIC!!
    return True


def main():
    import sys

    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = "PASS" if is_pal else "FAIL"
            is_str = "is" if is_pal else "is not"
            print("{}: {} {} a palindrome".format(result, repr(arg), is_str))
    else:
        print("Usage: {} string1 string2 ... stringN".format(sys.argv[0]))
        print("  checks if each argument given is a palindrome")


if __name__ == "__main__":
    main()
