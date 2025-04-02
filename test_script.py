import unittest
from script import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World! How are you today?")

if __name__ == "__main__":
    unittest.main()
