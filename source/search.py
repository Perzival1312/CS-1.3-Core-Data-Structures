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
    # Just to make debugging eaier
    sys.setrecursionlimit(75)
    # Pre-check if not in array b4 search
    # if item not in set(array):
    #     return None
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # count = 0
    # index = (len(array)-1) // 2
    # print(1 // 2)
    # prev_ind = len(array)-1
    # while count < 5:
    #     # if count > 0:
    #     #     # print(prev_ind, ' | ', index)
    #     #     prev_ind = index
    #     if item == array[index]:
    #         return index
    #     else:
    #         # prev_ind = index
    #         if item < array[index]:
    #             print('{} is before {} at index {}'.format(item, array[index], index), ' | c: ', count, ' | p: ', prev_ind)
    #             prev_ind = index
    #             index = index // 2
    #         else:
    #             print('{} is after  {} at index {}'.format(item, array[index], index), ' | c: ', count, ' | p: ', prev_ind)
    #             index = (index + prev_ind) // 2
    #     # prev_ind = index
    #     count += 1
    #     print('p ', prev_ind, ' | c', index)
    #     if prev_ind == index:
    #         # print(array.index(item))
    #         return None
        
        # print(index)

        right = len(array) - 1
        left = 0
        index = (right + left) // 2
        if array[0] == item:
            return 0
        while left < index and index < right:
            if item == array[index]:
                return index
            
            if array[index] > item:
                right = index - 1 
            else:
                left = index + 1

            index = (right + left) // 2

        return None



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
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    contain = 'Julia'
    not_contain = 'Jeremy'

    print(binary_search(names, contain))
    print(binary_search(names, not_contain))

if __name__ == '__main__':
    main()