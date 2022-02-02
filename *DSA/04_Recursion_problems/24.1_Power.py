"""
Write a func called power which accepts a base and exponent. 
The func should return the power of the base to the exponent. 
This func should mimic the functionality of math.pow()
do not worry about negative bases and exponents
"""


def power(base, exponent: int) -> float:
    if base in [0, 1]:
        return base 
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)