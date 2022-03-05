from dataclasses import dataclass

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