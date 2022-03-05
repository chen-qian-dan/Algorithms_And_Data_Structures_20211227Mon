import unittest

import os 
import pathlib
from Data import Data 

class Test_init(unittest.TestCase):
    def test_arg_type(self):
        with self.assertRaises(TypeError):
            _ = Data(path = 1, windowSize = 9) # <------ path should be str

        with self.assertRaises(TypeError):
            _ = Data(path = "", windowSize = 9.9) # <------ windowSize should be int

    
    def test_arg_value(self):
        with self.assertRaises(ValueError):
            _ = Data(path = "", windowSize = 0) # <------ windowSize should > 0



class Test_generator(unittest.TestCase):
    def test_windowSize_is_3(self):
        file_path = pathlib.Path(__file__).parent.absolute()
        oData = Data(path = os.path.join(file_path, "./test_data/close_prices.csv"), windowSize = 3)
        expected_lst = [None, 
                    None,
                    22.937,
                    23.077,
                    22.99,
                    23.037,
                    22.967,
                    23.12,
                    23.24,
                    23.397,
                    23.833,
                    24.24,
                    24.58,
                    24.29,
                    23.85,
                    23.523,
                    23.3,
                    23.28,
                    23.143,
                    23.057,
                    22.92]
        for i in range(len(expected_lst)):
            expected = expected_lst[i]
            _, _, actual, _ = next(oData.gen)
            if not actual is None:
                actual = round(actual, 3)
            self.assertAlmostEqual(expected, actual)








if __name__ == '__main__':
    unittest.main()