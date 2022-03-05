import pandas as pd
from Constants import OutputFields
from Data import Data 


class Trader:
    def __init__(self, input_csv: str, sma1_window: int, sma2_window: int, output_csv: str):
        # check type
        if not isinstance(input_csv, str):
            raise TypeError("input_csv must be string type")
        if not isinstance(sma1_window, int):
            raise TypeError("sma1_window must be int type")
        if not isinstance(sma2_window, int):
            raise TypeError("sma2_window must be int type")
        if not isinstance(output_csv, str):
            raise TypeError("output_csv must be string type")

        # check value 
        if sma1_window <= 0:
            raise ValueError("sma1_window > 0 must be True")
        if sma2_window <= 0:
            raise TypeError("sma2_window > 0  must be True")
        
        if sma1_window >= sma2_window:
            raise ValueError(f"sma1_window({sma1_window}) < sma2_window({sma2_window}) must be True")


        self.input_csv: str = input_csv
        self.sma1_window: int = sma1_window
        self.sma2_window: int = sma2_window
        self.output_csv: str = output_csv

    def run(self):

        oData1 = Data(self.input_csv, self.sma1_window)
        oData2 = Data(self.input_csv, self.sma2_window)

        df = pd.DataFrame(columns = [OutputFields.Date, OutputFields.ClosePrice, OutputFields.Sma1, OutputFields.Sma2, OutputFields.Position])
    

        for v1, v2 in zip(oData1.gen, oData2.gen):
            signal = 0 
            arg1 = 0
            arg2 = 0
            if v1[2] and v2[2]:
                arg1 = round(v1[2], 3)
                arg2 = round(v2[2], 3)
                if arg1 > arg2:
                    signal = 1
                elif arg1 < arg2:
                    signal = -1

            df.loc[len(df)] = [v1[0], v1[1], arg1, arg2, signal]

        df.to_csv(self.output_csv, index = False)