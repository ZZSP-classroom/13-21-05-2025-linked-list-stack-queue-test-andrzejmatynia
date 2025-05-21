import unittest
from call_center_4 import CallCenter

class TestCallCenter(unittest.TestCase):
    def setUp(self):
        self.call_center = CallCenter()

    def test_receive_and_process_call(self):
        self.call_center.receive_call("caller1","10:00")
        self.call_center.receive_call("caller2","10:05 AM")
        
        self.assertIsNotNone(self.call_center.process_call())
        self.assertIsNotNone(self.call_center.get_current_call())

    def test_end_call(self):
        self.call_center.receive_call("caller1","10:00")
        self.call_center.process_call()
        ended_call = self.call_center.end_call()
        
        self.assertEqual(ended_call.caller_id, "caller1")
        self.assertIsNone(self.call_center.get_current_call())

    def test_no_calls(self):
        self.assertIsNone(self.call_center.process_call())
        self.assertIsNone(self.call_center.end_call())
        self.assertIsNone(self.call_center.get_current_call())

if __name__ == "__main__":
    unittest.main()
