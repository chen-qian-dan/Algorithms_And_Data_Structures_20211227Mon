#!/bin/sh
import os
import sys 
import pathlib
from Trader import Trader 
 

parent_path = pathlib.Path(__file__).parent.absolute()
input_csv: str = os.path.join(parent_path, '../Input/close_prices.csv') 
sma1_window: int = 3
sma2_window: int = 9 
output_csv: str = 'output.csv'




if __name__ == '__main__':
    if len(sys.argv) == 1:
        oTrader: Trader = Trader(input_csv = input_csv, sma1_window = sma1_window, sma2_window = sma2_window, output_csv = output_csv)
        oTrader.run()

    elif len(sys.argv) == 5:
        oTrader: Trader = Trader(input_csv = sys.argv[1], sma1_window = int(sys.argv[2]), sma2_window = int(sys.argv[3]), output_csv = sys.argv[4])
        oTrader.run()
        
    else:
        print("The arguments are wrong: either give zero arguments or 4 arguments: <absolute path of input_csv>, sma1_window, sma2_window <absolute path of output_csv>")