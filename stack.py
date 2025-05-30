class Node:
    # constuctor
    def __init__(self, element):
        self.val = element
        self.prev = None

class Stack:
    # constructor
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, element):
        node = Node(element)

        self.len += 1
        if not self.head:
            self.head = node
            return
        node.prev = self.head
        self.head = node

    def pop(self):
        if not self.head: return None
        self.len -= 1
        head = self.head
        self.head = self.head.prev
        head.prev = None
        return head.val


    def peek(self):
        if self.head: return self.head.val
        return None

stack = Stack()
stack.push(1)
print(stack.peek())
stack.push(2)
print(stack.peek())
stack.push(3)
print(stack.peek())
stack.pop() # 3
stack.pop() # 2
print(stack.peek())
stack.pop() # 1 (stack should be empty now)
print(stack.peek())
stack.pop()
print(stack.peek())

"""
sour@OR3 super-journey % python3 stack.py
1
2
3
1
None
None
"""
