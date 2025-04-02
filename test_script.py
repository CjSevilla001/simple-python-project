import unittest
from script import greet  # Import the function to test

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")  # Expected output

if __name__ == "__main__":
    unittest.main()
