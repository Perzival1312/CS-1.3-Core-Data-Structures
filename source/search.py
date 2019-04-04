#!python
import math, sys

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    if item not in set(array):
        return None
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if item == array[index]:
        return index
    return linear_search_recursive(array, item, index+1)
    # pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # Garuntee Sorted
    array = sorted(array)
    # Just to make debigging eaier
    sys.setrecursionlimit(75)
    # Pre-check if not in array b4 search
    if item not in set(array):
        return None
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    
    index = len(array) // 2
    while True:
        if item == array[index]:
            return index
        else:
            if array[index] > item:
                index = index // 2
            else:
                index = (index + len(array)) // 2
        print(index)

    # if equal return index
    # else
    #   if more than 
    #       next_area = index//2
    #   else #less than
    #       next_area = math.floor(index * 1.5)
    # 
    # if next_area//2 == next_area --> return None.

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=0, right=None):

    # TODO: implement binary search recursively here
    if right == None:
        right = len(array)
    index = (left + right) // 2

    if item == array[index]:
        return index
    
    if array[index] > item:
        right = index
    else:
        left = index

    # print(index, left, '--', right)
    return binary_search_recursive(array, item, left, right)

    # pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


def main():
    names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
    contain = 'Julia'
    not_contain = 'Jeremy'

    print(binary_search(names, contain))
    print(binary_search(names, not_contain))

if __name__ == '__main__':
    main()