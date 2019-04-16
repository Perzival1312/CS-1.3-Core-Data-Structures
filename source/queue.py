#!python3

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – LL append is constant time - only reassign vars"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – reassign head var [TODO]"""
        if not self.is_empty():
            to_remove = self.list.head.data
            self.list.delete(to_remove)
            return to_remove
        raise ValueError('Queue is empty')


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Why? [TODO]"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if not self.is_empty():
            return self.list[0]
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if not self.is_empty():
            to_remove = self.list[0]
            self.list.remove(to_remove)
            return to_remove
        raise ValueError('Queue is empty')

class Deque(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_front(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def push_front(self, item):
        """add item to the front of the queue"""
        self.list.prepend(item)
    
    def push_back(self, item):
        """add item to the end of the queue"""
        self.list.append(item)
    
    def pop_front(self):
        """remove item from the front of the queue and return that value or
        raise a value error if the queue is empty"""
        if not self.is_empty():
            to_remove = self.list.head.data
            self.list.delete(to_remove)
            return to_remove
        raise ValueError('Queue is empty')
    
    def pop_back(self):
        """remove item from the back of the queue and return that value or
        raise a value error if the queue is empty"""
        if not self.is_empty():
            to_remove = self.list.tail.data
            self.list.delete(to_remove)
            return to_remove
        raise ValueError('Queue is empty')

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def back(self):
        """Return the item at the back of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.tail.data

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
Dequeue = Deque
