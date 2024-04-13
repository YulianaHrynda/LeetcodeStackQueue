"""
Queue using Stacks
"""

class Node:
    """Node"""
    def __init__(self, item, next=None):
        """Initializes a new instance of Node with given item and next node reference."""
        self.item = item
        self.next = next

class Stack:
    """Stack"""
    def __init__(self):
        """Initializes a new instance of Stack with an empty stack."""
        self.head = None

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return self.head is None

    def push(self, item):
        """Pushes an item onto the top of the stack."""
        self.head = Node(item, self.head)

    def pop(self):
        """Removes and returns the item at the top of the stack."""
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        """Returns the item at the top of the stack without removing it."""
        return self.head.item

    def __len__(self):
        """Returns the number of items currently in the stack."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """Returns a string representation of the stack from bottom to top."""
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' + s
            cur = cur.next
        return 'bottom -> ' + s + '<- top'

class MyQueue:
    """MyQueue"""
    def __init__(self):
        """
        Initializes a new instance of the MyQueue class with two empty stacks.
        """
        self.stack_push = Stack()  # Stack to store elements pushed into the queue.
        self.stack_pop = Stack()   # Stack to store elements for popping from the queue.

    def push(self, x: int) -> None:
        """
        Pushes an element x to the back of the queue by pushing it onto the stack_push.
        """
        self.stack_push.push(x)

    def pop(self) -> int:
        """
        Removes and returns the element from the front of the queue by transferring elements from stack_push to stack_pop if necessary.
        """
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Returns the element at the front of the queue without 
        removing it, by transferring elements from stack_push 
        to stack_pop if necessary.
        """
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.peek

    def empty(self) -> bool:
        """
        Returns True if the queue is empty, otherwise returns False.
        """
        return self.stack_pop.is_empty() and self.stack_push.is_empty()
