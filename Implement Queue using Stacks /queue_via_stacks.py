class Node:
    """
    Represents a node in a linked list.

    Attributes:
        item (any): The data stored in the node.
        next (Node, optional): A reference to the next node in the sequence. Defaults to None.
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    """
    Implements a Last-In-First-Out (LIFO) stack using a linked list.

    Attributes:
        head (Node): The top node of the stack, or None if empty.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.head is None

    def push(self, item):
        """
        Pushes a new item onto the stack.

        Args:
            item (any): The item to be added.
        """
        self.head = Node(item, self.head)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Returns:
            any: The item that was removed from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        """
        Returns the top item of the stack without removing it.

        Returns:
            any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.item

    def __len__(self):
        """
        Returns the number of items in the stack.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """
        Returns a string representation of the stack, showing the order from bottom to top.
        """
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' + s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'
    
class MyQueue:
    """
    Implements a First-In-First-Out (FIFO) queue using two stacks.

    Attributes:
        stack_push (Stack): A stack used to temporarily store elements for enqueueing.
        stack_pop (Stack): A stack used to store elements for dequeueing.
    """
    def __init__(self):
        self.stack_push = Stack()
        self.stack_pop = Stack()
        

    def push(self, x: int) -> None:
        """
        Adds an item (x) to the back of the queue.

        Args:
            x (int): The item to be added.
        """
        self.stack_push.push(x)

    def pop(self) -> int:
        """
        Removes and returns the front item from the queue.

        Returns:
            int: The item that was removed from the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        if self.stack_pop.is_empty():
            raise IndexError("pop from empty queue")
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Returns the front item of the queue without removing it.

        Returns:
            int: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
