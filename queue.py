class Node:
    # constructor
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    # constructor
    def __init__(self):
        self.tail = self.head = None
        self.len = 0

    def enqueue(self, element):
        node = Node(element)
        self.len += 1
        if not self.tail:
            self.tail = self.head = node
            return
        self.tail.next = node
        self.tail = self.tail.next

    def deque(self):
        if not self.head: return None
        self.len -= 1
        dummy = self.head
        self.head = self.head.next

        # free
        dummy.next = None
        if self.len == 0: self.tail = None

        return dummy.value


    def peek(self):
        if self.head: return self.head.value
        return None


q = Queue()
q.enqueue(5)
q.enqueue(6)
print(q.deque())
print(q.peek())

"""
A -> B -> C
^         ^
h         t
enqueue at the tail
dequeue from head

sour@OR3 super-journey % python3 queue.py
5
6
"""
