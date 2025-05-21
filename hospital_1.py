class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, patient):
        new_node = Node(patient)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
 
    def dequeue(self):
        if self.front is None:
            return None
        removed_patient = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_patient

    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
