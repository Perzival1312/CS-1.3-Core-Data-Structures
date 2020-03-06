#!python3

from hashtable import HashTable

class InheritSet(set):
    def __init__(self, elements=None):
        self.container = super()
        self.size = 0
        if elements is not None:
            self.size = len(elements)
            for item in elements:
                self.container.add(item)
        
    
    def add(self, element):
        self.size += 1
        super().add(element)
    
    def remove(self, element):
        self.size -= 1
        super().remove(element)
    
    def union(self, other_set):
        return InheritSet(super().union(other_set))
    
    def intersection(self, other_set):
        return InheritSet(super().intersection(other_set))
    
    def difference(self, other_set):
        return InheritSet(super().difference(other_set))

    def is_subset(self, other_set):
        return super().issubset(other_set)



# hashtable init call in resize calls this sets init
# even though printing self the line before prints a 
# hashtable so not too sure about this
# also this is bad bc its exposing a LOT of methods 
# it shouoldn't.
class dictSet(HashTable):
    def __init__(self, elements=None):
        super().__init__()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.size += 1
                self.set(item, None)





class arraySet():
    def __init__(self, elements=None):
        self.size = 0
        self.container = Array()
        if elements is not None:
            for item in elements:
                self.container.append(item)
                self.size += 1

    def __contains__(self, element):
        # NEEDS TO BE CONSTANT TIME!!!! therefore hashtable underlying datatype
        for item in self.container:
            if item == element:
                return True
        return False
    
#     add(element) - add element to this set, if not present already
    def add(self, element):
        self.size += 1
        self.container.append(element)
    
#     remove(element) - remove element from this set, if present, or else raise KeyError
    def remove(self, element):
        self.size -= 1
        self.container.remove(element)
    
#     union(other_set) - return a new set that is the union of this set and other_set
    def union(self, other_set):
        union = arraySet()
        print(self.container)
        for item in self.container:
            union.add(item)

        for item in other_set.container:
            if item not in union:
                union.add(item)
        return union

#     intersection(other_set) - return a new set that is the intersection of this set and other_set
    def intersection(self, other_set):
        inter = arraySet()
        for item in self.container:
            if item in other_set:
                inter.add(item)
        return inter
        
#     difference(other_set) - return a new set that is the difference of this set and other_set
    def difference(self, other_set):
        diff = arraySet()
        for item in self.container:
            if item not in other_set:
                diff.add(item)
        return diff

#     is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
    def is_subset(self, other_set):
        for item in self.container:
            if item not in other_set:
                return False
        return True






















































# this seems really hacky to modify the builtin list class
# TODO: check for accepability.
class Array(list):
    def __init__(self, elements=None):
        if elements is not None:
            super().__init__(elements)
        else:
            super().__init__()
    
    def items(self):
        return self

    def keys(self):
        return self

    def values(self):
        return self


class MySet(object):
#     __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given
    def __init__(self, elements=None):
        self.container = Hashtable()
#     size - property that tracks the number of elements in constant time
        self.size = self.container.size
        if elements is not None:
            print(elements)
            for item in elements:
                self.size += 1
                self.container.set(item, None)
    
    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ["{!r}".format(key) for key, _ in self.container.items()]
        return "{" + ", ".join(items) + "}"
    
    def __iter__(self):
        return self.container.__iter__()

# return a boolean indicating whether element is in this set
    def __contains__(self, element):
        # Needs to be constant time to be efficient
        return self.container.contains(element)
    
    def contains(self, element):
        return element in self.container
    
# add element to this set, if not present already
    def add(self, element):
        self.size += 1
        self.container.set(element, None)
    
# remove element from this set, if present, or else raise KeyError
    def remove(self, element):
        self.size -= 1
        self.container.delete(element)
    
# return a new set that is the union of this set and other_set
    def union(self, other_set):
        union = MySet()

        for key, _ in self.container.items():
            union.add(key)

        for key, _ in other_set.container.items():
            if key not in union:
                union.add(key)
        return union

    
# return a new set that is the intersection of this set and other_set
    def intersection(self, other_set):
        union = MySet()
        for key, _ in self.container.items():
            if key in other_set:
                union.add(key)
        return union
        
    
# return a new set that is the difference of this set and other_set
    def difference(self, other_set):
        union = MySet()
        for key, _ in self.container.items():
            if key not in other_set:
                union.add(key)
        return union

#     is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set
    def is_subset(self, other_set):
        for key, _ in self.container.items():
            if key not in other_set:
                return False
        return True
