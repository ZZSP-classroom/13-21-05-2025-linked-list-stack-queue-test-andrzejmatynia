import unittest
from hospital_1 import Queue, Patient

class TestQueue(unittest.TestCase):


    def setUp(self):
        self.queue = Queue()
        self.patient1 = Patient("a", "10:00")
        self.patient2 = Patient("b", "10:30")
        self.patient3 = Patient("c", "11:00")

    def test_enqueue(self):
        self.queue.enqueue(self.patient1)
        self.queue.enqueue(self.patient2)
        self.assertEqual(self.queue.get_size(), 2)

    def test_dequeue(self):
        self.queue.enqueue(self.patient1)
        self.queue.enqueue(self.patient2)
        removed_patient = self.queue.dequeue()
        self.assertEqual(removed_patient.name, "a")
        self.assertEqual(self.queue.get_size(), 1)

    def test_peek(self):
        self.queue.enqueue(self.patient1)
        self.queue.enqueue(self.patient2)
        self.assertEqual(self.queue.peek().name, "a")

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(self.patient1)
        self.assertFalse(self.queue.is_empty())
if __name__ == "__main__":
    unittest.main()
