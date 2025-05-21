import unittest
from task_scheduler_5 import PriorityQueue, Task

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_add_and_process_task(self):
        self.pq.add_task(Task("Task 1", 2))
        self.pq.add_task(Task("Task 2", 1))
        self.pq.add_task(Task("Task 3", 3))

        self.assertEqual(self.pq.process_task().task_name, "Task 2")
        self.assertEqual(self.pq.process_task().task_name, "Task 1")
        self.assertEqual(self.pq.process_task().task_name, "Task 3")
        self.assertIsNone(self.pq.process_task())

    def test_empty_queue(self):
        self.assertIsNone(self.pq.process_task())

if __name__ == "__main__":
    unittest.main()
