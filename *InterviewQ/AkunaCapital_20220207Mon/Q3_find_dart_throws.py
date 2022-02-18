#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List



#
# Complete the 'find_dart_throws' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER score as parameter.
#

SCORES = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "11",
    12: "12",
    13: "13",
    14: "14",
    15: "15",
    16: "16",
    17: "17",
    18: "18",
    19: "19",
    20: "20",
    21: "t7",
    22: "d11",
    24: "d12",
    25: "outer",
    26: "d13",
    27: "t9",
    28: "d14",
    30: "d15",
    32: "d16",
    33: "t11",
    34: "d17",
    36: "d18",
    38: "d19",
    39: "t13",
    40: "d20",
    42: "t14",
    45: "t15",
    48: "t16",
    50: "bull",
    51: "t17",
    54: "t18",
    57: "t19",
    60: "t20",
}

def find_dart_throws(score: int) -> List[str]:
    # Write your code here
    if score in SCORES.keys():
        return [SCORES[score]]
    
    s = list(SCORES.keys())
    ret = list()
    while score > 0:
        b = find_biggest(s, score)
        ret.append(SCORES[b])
        score -= b
        
    return ret 
    
    
def find_biggest(s: List[int], score: int) -> int:
    # find the biggest key that < score
    index = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] <= score:
            index = i
            break 
    biggest = s[index]
    return biggest
            
        
print(find_dart_throws(170))