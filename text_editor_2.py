class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, operation):
        new_node = Node(operation)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        popped_operation = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_operation

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
