#!/bin/sh
import os
import sys 
import pathlib
import pandas as pd
from Constants import OutputFields
from Data import Data 
 


def execuate(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str):

    # output_path = os.path.join(parent_path, output_csv) 
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)

    oData1 = Data(os.path.join(parent_path, input_csv), sma1_window)
    oData2 = Data(os.path.join(parent_path, input_csv), sma2_window)

    df = pd.DataFrame(columns = [OutputFields.Date, OutputFields.ClosePrice, OutputFields.Sma1, OutputFields.Sma2, OutputFields.Position])
   

    for v1, v2 in zip(oData1.gen, oData2.gen):
        signal = 0 
        if v1[2] and v2[2]:
            if v1[2] > v2[2]:
                signal = 1
            elif v1[2] < v2[2]:
                signal = -1

        df.loc[len(df)] = [v1[0], v1[1], v1[2], v2[2], signal]

    df.to_csv(output_csv, index = False )
    
    print(input_csv)



# def trade(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str):
#     execuate(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str)



parent_path = pathlib.Path(__file__).parent.absolute()
input_csv: str = os.path.join(parent_path, '../Input/close_prices.csv') 
sma1_window: int = 3
sma2_window: int = 9 
output_csv: str = 'output.csv'




if __name__ == '__main__':
    if len(sys.argv) == 1:
        execuate(input_csv, sma1_window, sma2_window, output_csv)
    elif len(sys.argv) == 5:
        execuate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    else:
        print("The arguments are wrong: either give zero arguments or 4 arguments: <absolute path of input_csv>, sma1_window, sma2_window <absolute path of output_csv>")