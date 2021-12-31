"""
How many day's temperature? 2
Day 1's high temp: 10
Day 2's high temp: 20

Average = 15.0
1 day(s) above average
"""

from typing import List

def calculate_average_temperature():
    nDayCount: int = int(input("How many day's temperature? "))

    fTempLst: List[float] = list()
    for nDay in range(nDayCount):
        fTempLst.append(float(input(f"Day {nDay + 1}'s high temp: ")))
    
    fAverage: float = sum(fTempLst) / nDayCount
    print(f"Average = {fAverage}\n")

    # calculate days above average temp
    nAboveTempDays: int = 0
    for v in fTempLst:
        if v > fAverage:
            nAboveTempDays += 1
    print(f"{nAboveTempDays} day(s) above average")


calculate_average_temperature()

