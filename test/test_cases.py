import unittest

from my_module import MyFunction


class MyFunctionTestCase(unittest.TestCase):
    def test_valid_input(self):
        # Test case for valid input
        result = MyFunction(5)
        self.assertEqual(result, 10)

    def test_invalid_input(self):
        # Test case for invalid input
        with self.assertRaises(ValueError):
            MyFunction(-5)

    def test_edge_case(self):
        # Test case for edge case
        result = MyFunction(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
