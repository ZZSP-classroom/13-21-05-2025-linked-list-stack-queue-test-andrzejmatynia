class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

    def __repr__(self):
        return f"Call(caller_id={self.caller_id}, time_received={self.time_received})"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, call):
        new_node = Node(call)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return None
        removed_call = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_call

    def is_empty(self):
        return self.size == 0


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, call):
        new_node = Node(call)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        popped_call = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_call

    def is_empty(self):
        return self.size == 0


class CallCenter:
    def __init__(self):
        self.call_queue = Queue()
        self.call_stack = Stack()

    def receive_call(self, caller_id, time_received):
        call = Call(caller_id, time_received)
        self.call_queue.enqueue(call)

    def process_call(self):
        if not self.call_queue.is_empty():
            call = self.call_queue.dequeue()
            self.call_stack.push(call)
            return call
        return None

    def end_call(self):
        return self.call_stack.pop()

    def get_current_call(self):
        return self.call_stack.top.data if not self.call_stack.is_empty() else None

