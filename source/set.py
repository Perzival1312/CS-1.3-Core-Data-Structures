#!python3

    # Implement Set class (abstract data type backed by data structure of your choice) with the following set operations as instance methods and properties:
    #     __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given
    #     size - property that tracks the number of elements in constant time
    #     contains(element) - return a boolean indicating whether element is in this set
    #     add(element) - add element to this set, if not present already
    #     remove(element) - remove element from this set, if present, or else raise KeyError
    #     union(other_set) - return a new set that is the union of this set and other_set
    #     intersection(other_set) - return a new set that is the intersection of this set and other_set
    #     difference(other_set) - return a new set that is the difference of this set and other_set
    #     is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
    # Write unit tests to ensure the Set class is robust
    #     Include test cases for each class instance method
    # Annotate all instance methods with complexity analysis of running time and space (memory)
    # Compare the behaviors of your Set class to those of the Python set type and Swift Set type

from hashtable import HashTable

class InheritSet(set):
    def __init__(self, elements=None):
        super().__init__()
        
        if elements is not None:
            for item in elements:
                super().add(item)
        
        # self.size = 0
    
    # def __contains__(self, element):
    #     return super().__contains__(element)
    
    # def add(self, element):
    #     super().add(element)
    
    # def remove(self, element):
    #     super().remove(element)
    
    # def union(self, other_set):
    #     return super().union(other_set)
    
    # def intersection(self, other_set):
    #     return super().intersection(other_set)
    
    # def difference(self, other_set):
    #     return super().difference(other_set)

    def is_subset(self, other_set):
        return super().issubset(other_set)





















































# Write unit tests to ensure the Set class is robust
#     Include test cases for each class instance method
# Annotate all instance methods with complexity analysis of running time and space (memory)
# Compare the behaviors of your Set class to those of the Python set type and Swift Set type

class MySet(object):
#     __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given
    def __init__(self, elements=None):
        # super().__init__()
        self.container = HashTable()
#     size - property that tracks the number of elements in constant time
        self.size = 0
        if elements is not None:
            print(elements)
            for item in elements:
                self.size += 1
                self.container.set(item, None)

#     contains(element) - return a boolean indicating whether element is in this set
    def __contains__(self, element):
        # NEEDS TO BE CONSTANT TIME!!!! therefore hashtable underlying datatype
        return self.container.contains(element)
    
#     add(element) - add element to this set, if not present already
    def add(self, element):
        self.container.set(element, None)
    
#     remove(element) - remove element from this set, if present, or else raise KeyError
    def remove(self, element):
        self.container.delete(element)
    
#     union(other_set) - return a new set that is the union of this set and other_set
    def union(self, other_set):
        pass
    
#     intersection(other_set) - return a new set that is the intersection of this set and other_set
    def intersection(self, other_set):
        pass
    
#     difference(other_set) - return a new set that is the difference of this set and other_set
    def difference(self, other_set):
        pass

#     is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
    def is_subset(self, other_set):
        pass



