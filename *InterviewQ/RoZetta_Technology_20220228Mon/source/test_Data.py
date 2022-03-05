import unittest
from Data import Data 

class Test_init(unittest.TestCase):
    def test_arg_type(self):
        with self.assertRaises(TypeError):
            _ = Data(path = 1, windowSize = 9) # <------ path should be str

        with self.assertRaises(TypeError):
            _ = Data(path = "", windowSize = 9.9) # <------ windowSize should be int




if __name__ == '__main__':
    unittest.main()