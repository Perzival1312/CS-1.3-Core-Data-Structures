#!python
import math, sys

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # Just to make debugging eaier
    sys.setrecursionlimit(75)
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    # check if index to check is even in array
    if index > len(array) - 1:
        return None
    # check if index is correct for item
    if item == array[index]:
        return index
    # recursive call
    return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # Garuntee Sorted
    array = sorted(array)
    # Just to make debugging eaier
    sys.setrecursionlimit(75)
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

def binary_search_iterative(array, item):
    # create left and right bounds
    right = len(array) - 1
    left = 0
    # get index to check
    index = (right + left) // 2

    while left <= index and index <= right:
        # check if index is correct for item
        if item == array[index]:
            return index
        # else find where item is in relation to index and adjust bounds accordingly
        if array[index] > item:
            right = index - 1 
        else:
            left = index + 1
        # adjust index based on new bounds
        index = (right + left) // 2
    # item not found so return none
    return None

def binary_search_recursive(array, item, left=0, right=None):
    # assign right bound in initial run
    if right == None:
        right = len(array)
    # set index based on bounds
    index = (left + right) // 2
    # check if index is correct for item
    if item == array[index]:
        return index
    # else find where item is in relation to index and adjust bounds accordingly
    if array[index] > item:
        right = index
    else:
        left = index
    # recursive call
    return binary_search_recursive(array, item, left, right)

# callable from command liine
def main():
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    contain = 'Julia'
    not_contain = 'Jeremy'

    print(binary_search(names, contain))
    print(binary_search(names, not_contain))

if __name__ == '__main__':
    main()