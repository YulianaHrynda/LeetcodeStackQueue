class Node:
    """Represents a single element in a linked list."""
    def __init__(self, item, next=None):
        """Initializes a new instance of Node with given item and next node reference."""
        self.item = item
        self.next = next

class Queue:
    """Implements a queue data structure using a linked list."""
    def __init__(self):
        """Initializes an empty queue."""
        self.head = None
        self.tail = None

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.head is None

    def add(self, item):
        """Adds an item to the end of the queue."""
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        """Removes and returns the item at the front of the queue."""
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        """Returns the item at the front of the queue without removing it."""
        return self.head.item

    def __len__(self):
        """Returns the number of items in the queue."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """Returns a string representation of the queue."""
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'


class MyStack:
    def __init__(self):
        """Initializes two queues: queue_push and queue_pop."""
        self.queue_push = Queue()
        self.queue_pop = Queue()

    def push(self, x: int) -> None:
        """Pushes an element onto the stack."""
        self.queue_push.add(x)

    def pop(self) -> int:
        """Removes and returns the element on top of the stack."""
        if self.empty():
            raise ValueError('Stack is empty')

        while len(self.queue_push) > 1:
            self.queue_pop.add(self.queue_push.pop().item)

        value = self.queue_push.pop().item

        self.queue_push, self.queue_pop = self.queue_pop, self.queue_push
        return value

    def top(self) -> int:
        """Returns the element on top of the stack without removing it."""
        if self.empty():
            raise ValueError('Stack is empty')

        while len(self.queue_push) > 1:
            self.queue_pop.add(self.queue_push.pop().item)
        
        top = self.queue_push.peek

        self.queue_pop.add(self.queue_push.pop().item)
        self.queue_push, self.queue_pop = self.queue_pop, self.queue_push
        return top

    def empty(self) -> bool:
        """Checks if the stack is empty."""
        return self.queue_push.is_empty() and self.queue_pop.is_empty()
