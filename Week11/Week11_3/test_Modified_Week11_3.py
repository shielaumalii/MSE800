import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        # self.assertEqual('foo'.upper(), 'BAR')  # This will fail
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_isdigit(self):
        self.assertTrue('123'.isdigit())

if __name__ == '__main__':
    unittest.main()
