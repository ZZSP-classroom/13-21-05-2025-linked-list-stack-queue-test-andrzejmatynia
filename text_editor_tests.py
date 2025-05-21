import unittest
from text_editor_2 import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push("typed 'hello'")
        self.stack.push("typed 'world'")
        self.assertEqual(self.stack.get_size(), 2)

    def test_pop(self):
        self.stack.push("typed 'hello'")
        self.stack.push("typed 'world'")
        removed_operation = self.stack.pop()
        self.assertEqual(removed_operation, "typed 'world'")
        self.assertEqual(self.stack.get_size(), 1)

    def test_peek(self):
        self.stack.push("typed 'hello'")
        self.stack.push("typed 'world'")
        self.assertEqual(self.stack.peek(), "typed 'world'")

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push("typed 'hello'")
        self.assertFalse(self.stack.is_empty())

if __name__ == "__main__":
    unittest.main()
