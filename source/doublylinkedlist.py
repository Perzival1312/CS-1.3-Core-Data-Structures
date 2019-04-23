class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None  # an OBJECT
        self.prev = None  # an OBJECT

    def __repr__(self):
        """Return a string representation of this node."""
        return "Node({!r})".format(self.data)


class LListIter(object):
    def __init__(self, item):
        self.item = item

    def __next__(self):
        node = self.item
        if node == None:
            raise StopIteration
        self.item = self.item.next
        return node


class DblLinkedList(object):
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" <-> ".join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return "LinkedList({!r})".format(self.items())

    def __iter__(self):
        return LListIter(self.head)

    def __len__(self):
        return self.size + 1

    def __getitem__(self, ind):
        if not (0 <= ind < self.size):
            raise ValueError("List index out of range: {}".format(ind))
        node = self.head
        if ind > 0:
            for _ in range(ind):
                node = node.next
        return node
    
    def get_at_index(self, ind):
        # make similar to singly linked list
        return self[ind].data

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        # O(1)
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) Why and under what conditions?
                searching through all nodes"""
        return self.size

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) just changing var values
        Worst case running time: O(1) just changing var values"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError("List index out of range: {}".format(index))
        # at beginning
        if index == 0:
            self.prepend(item)
        # at end
        elif index == self.size:
            self.append(item)
        # in middle
        else:
            new_node = Node(item)
            self.size += 1
            current = self[index]
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Why and under what conditions?
                just changes some values"""
        if type(item) != Node:
            new_node = Node(item)
        else:
            new_node = item
        if self.tail is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Why and under what conditions?
                just changes some values"""
        if type(item) != Node:
            new_node = Node(item)
        else:
            new_node = item
        if self.head is not None:
            temp_node = self.head
            temp_node.prev = new_node
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) Why and under what conditions?
                quality is head only chacking once
        Worst case running time: O(n) Why and under what conditions?
                quality is tail checking entire list                     """
        node = self.head  # gets first element in linked list
        while node is not None:  # checks to see if it is a node
            if quality(
                node.data
            ):  # runs quality func which chacks if node data is equal to func input
                return node.data  # if true returning nodes data
            node = node.next  # next node
        return None  # default if not found

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) Why and under what conditions?
                item is head therefore only chcking once
        Worst case running time: O(n) Why and under what conditions?
                item is tail chcking entire ll"""

        node = self.head
        try:
            prev_node = node.prev
        except:
            prev_node = None
        while node is not None:
            if node.data == item:
                try:
                    prev_node.next = node.next
                except:
                    pass
                if node == self.head:
                    self.head = node.next
                    try:
                        self.head.prev = None
                    except:
                        pass
                try:
                    if node.data == self.tail.data:
                        self.tail = prev_node
                except:
                    pass
                node.next = None
                self.size -= 1
                break
            prev_node = node
            node = node.next
        else:
            raise ValueError("Item not found: {}".format(item))

    def replace(self, old, new):
        node = self.head
        while node is not None:
            if node.data == old:
                node.data = new
                break
            node = node.next
        else:
            raise ValueError("Item not found: {}".format(old))


def test_linked_list():
    ll = DblLinkedList(["A", "B", "C"])
    print("list: {}".format(ll))

    print("\nTesting append:")
    for item in ["D", "E", "F"]:
        print("append({!r})".format(item))
        ll.append(item)
        print("list: {}".format(ll))

    print("head: {}".format(ll.head))
    print("tail: {}".format(ll.tail))
    print("length: {}".format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print("\nTesting delete:")
        for item in ["B", "C", "A"]:
            print("delete({!r})".format(item))
            ll.delete(item)
            print("list: {}".format(ll))

        print("head: {}".format(ll.head))
        print("tail: {}".format(ll.tail))
        print("length: {}".format(ll.length()))

    ll.replace("D", "G")
    print(ll)
    # for items in ll:
    # #     for item in ll:
    #     print(items)
    for items in reversed(ll):
        #     for item in ll:
        print(items)
    # print(ll[6])
    # print(item)
    # print(ll)


if __name__ == "__main__":
    test_linked_list()
