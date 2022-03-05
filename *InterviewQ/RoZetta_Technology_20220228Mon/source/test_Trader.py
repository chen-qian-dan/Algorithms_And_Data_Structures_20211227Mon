import unittest

from Trader import Trader 

class Test_init(unittest.TestCase):
    def test_arg_type(self):
        with self.assertRaises(TypeError):
            _ = Trader(input_csv = 4,  # <--- should be str
                        sma1_window = 3, 
                        sma2_window = 9, 
                        output_csv = "")

        with self.assertRaises(TypeError):
            _ = Trader(input_csv = "",  
                        sma1_window = 3.5, # <--- should be int 
                        sma2_window = 9, 
                        output_csv = "")

        with self.assertRaises(TypeError):
            _ = Trader(input_csv = "",  
                        sma1_window = 3, 
                        sma2_window = 9.0, # <--- should be int 
                        output_csv = "")
    
        with self.assertRaises(TypeError):
            _ = Trader(input_csv = "",  
                        sma1_window = 3, 
                        sma2_window = 9, 
                        output_csv = 0) # <--- should be str

    def test_arg_value(self):
        with self.assertRaises(ValueError):
             _ = Trader(input_csv = "",  
                        sma1_window = 0,  # <--- should > 0
                        sma2_window = 9, 
                        output_csv = "")


        with self.assertRaises(ValueError):
             _ = Trader(input_csv = "",  
                        sma1_window = 3,  
                        sma2_window = 0,  # <--- should > 0
                        output_csv = "")




if __name__ == '__main__':
    unittest.main()