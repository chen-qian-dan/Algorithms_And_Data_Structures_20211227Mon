#!/bin/sh
import os
import sys 
import pathlib
import pandas as pd
from collections import deque 
from dataclasses import dataclass
 




def execuate(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str):

    parent_path = pathlib.Path(__file__).parent.absolute()

    oData1 = Data(os.path.join(parent_path, input_csv), sma1_window)
    oData2 = Data(os.path.join(parent_path, input_csv), sma2_window)

    dp = dict()
    for v in OutputFields:
        dp.setdefault(v, [])

    for v1, v2 in zip(oData1.gen, oData2.gen):
        print(v1)

    print(input_csv)



# def trade(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str):
#     execuate(input_csv: str, sma1_window: int, sma2_window: int, output_csv: str)


class Data:
    def __init__(self, path: str, windowSize: int):
        self.path = path
        self.windowSize = windowSize
        self.gen = self.generator()
        # for a in self.gen:
        #     print(a)
    


    def generator(self):
        """
        sliding window to calculate the average 
        """
        df = pd.read_csv(self.path)
        q = deque()
        avg = None 
        avg_old = None 
        status = None 
        for i in range(df.shape[0]):
            q.append(df[InputFields.Date][i])
  
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

            

@dataclass
class InputFields:
    Date: str = 'date'
    ClosePrice: str = 'close'



@dataclass
class OutputFields:
    Date: str = 'date'
    ClosePrice: str = 'close'
    Sma1: str = 'sma1'
    Sma2: str = 'sma2'
    Position: str = 'position'


input_csv: str = './Input/close_prices.csv'
sma1_window: int = 3
sma2_window: int = 9 
output_csv: str = './Output/output.csv'

execuate(input_csv, sma1_window, sma2_window, output_csv)


# if __name__ == '__main__':
#     execuate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])