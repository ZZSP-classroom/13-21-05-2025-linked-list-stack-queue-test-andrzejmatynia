class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority

    def __repr__(self):
        return f"Task(task_name={self.task_name}, priority={self.priority})"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if self.head is None or self.head.data.priority > task.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data.priority <= task.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def process_task(self):
        if self.head is None:
            return None
        task_to_process = self.head.data
        self.head = self.head.next
        return task_to_process

    def is_empty(self):
        return self.head is None
