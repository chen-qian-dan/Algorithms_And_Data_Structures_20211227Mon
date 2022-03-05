import pandas as pd
from collections import deque 
from Constants import InputFields

class Data:
    def __init__(self, path: str, windowSize: int):
        if not isinstance(path, str):
            raise TypeError("path must be string")
        if not isinstance(windowSize, int):
            raise TypeError("windowSize must be int type")
        
        if windowSize <= 0:
            raise ValueError("windowSize > 0 must be True")
            
        self.path = path
        self.windowSize = windowSize
        self.gen = self.generator()
       

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