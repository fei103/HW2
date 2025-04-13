import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

