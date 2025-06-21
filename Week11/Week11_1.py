"""Unit testing is a software testing technique where individual 
components or functions of a program are tested in isolation to 
ensure they behave as expected. In the example provided, the add(x, y) 
function is tested using Python's built-in unittest module. 
The class TestMathOperations inherits from unittest.TestCase 
and includes the method test_add, which checks if the add function 
returns correct results for given inputs. If any assertion fails, 
the test suite will report it, helping developers catch bugs early and 
maintain reliable code."""


# Import the built-in unittest module
import unittest

# A simple function that returns the sum of two numbers
def add(x, y):
    return x + y

# Create a test case class inheriting from unittest.TestCase
class TestMathOperations(unittest.TestCase):

    # Define a test method to test the 'add' function
    def test_add(self):
        # Test case 1: 2 + 3 should equal 5
        self.assertEqual(add(2, 3), 5)

        # Test case 2: -1 + 1 should equal 0
        self.assertEqual(add(-1, 1), 0)

# Run the tests when this script is executed directly
if __name__ == '__main__':
    unittest.main()
