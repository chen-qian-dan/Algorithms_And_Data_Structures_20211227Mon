#!/bin/sh
import os
import sys 
import pathlib
import pandas as pd
from collections import deque 
from Constants import OutputFields, InputFields
 


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


class Data:
    def __init__(self, path: str, windowSize: int):
        self.path = path
        self.windowSize = windowSize
        self.gen = self.generator()
       
    


    def generator(self):
        """
        sliding window to calculate the average 
        """
        df = pd.read_csv(self.path)
        print(self.path)
        q = deque()
        avg = None 
        avg_old = None 
        status = None 
        for i in range(df.shape[0]):
            q.append(df[InputFields.ClosePrice][i])
  
            if len(q) == self.windowSize:
                avg = sum(list(q)) / self.windowSize 
            elif len(q) >= self.windowSize:
                avg_old = avg 
                v = q.popleft()
                avg = avg + (df[InputFields.ClosePrice][i] - v) / self.windowSize

            if avg_old and avg:
                if avg > avg_old:
                    status = 1
                elif avg == avg_old:
                    status = 0 
                else:
                    status = -1 
            yield (df[InputFields.Date][i], df[InputFields.ClosePrice][i], avg, status)

            



parent_path = pathlib.Path(__file__).parent.absolute()
input_csv: str = os.path.join(parent_path, '../Input/close_prices.csv') 
sma1_window: int = 3
sma2_window: int = 9 
output_csv: str = 'output.csv'




if __name__ == '__main__':
    if len(sys.argv) == 1:
        execuate(input_csv, sma1_window, sma2_window, output_csv)
    else:
        execuate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])