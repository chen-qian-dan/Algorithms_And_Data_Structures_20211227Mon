import unittest
from Data import Data 

class Test_init(unittest.TestCase):
    def test_arg_type(self):
        with self.assertRaises(TypeError):
            _ = Data(path = 1, windowSize = 9) # <------ path should be str




if __name__ == '__main__':
    unittest.main()