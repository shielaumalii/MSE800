import unittest

class TestStringMethods(unittest.TestCase):

    """This test checks if the upper() method correctly converts a lowercase string to uppercase. 
    It verifies that 'foo'.upper() returns 'FOO'."""
    def test_upper(self): # Test if the string is converted to uppercase
        self.assertEqual('foo'.upper(), 'FOO')

    """This test validates the isupper() method by checking two conditions - 
    that 'FOO'.isupper() returns True (since all letters are uppercase) 
    and 'Foo'.isupper() returns False (since it contains lowercase letters)."""
    def test_isupper(self): 
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    """This test examines the split() method in two ways. 
    First, it confirms that 'hello world'.split() returns ['hello', 'world']. 
    Second, it uses assertRaises() to verify that calling split(2) 
    with an integer argument raises a TypeError."""
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
