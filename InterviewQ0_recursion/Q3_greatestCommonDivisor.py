# Q3_greatestCommonDivisor.py
"""
How to find greatest common divisor of two numbers using recursion?
1. problem: the greates common divisor of 8 and 4 is 4; 
    9 and 1 is 1
2. intput: positive integer 
3. output: positive integer 
4. edge case:
    8 and 4 is 4
    9 and 1 is 1
    0 and 0 is what? (eliminate it)
    9 and 0 is what? 9
    9 and -3 is 3
5. time complexity
6. space complexity 

Euclidean algorithm

gcd(48, 18)
step1: 48 / 18 = 2 remainder 12
step2: 18 / 12 = 1 remainder 6
step3: 12 / 6 = 2 remainder 0
so, gcd(48, 18) = 6
"""

def getGreatestCommonDivisor(A: int, B: int) -> int:
    if not isinstance(A, int) or not isinstance(B, int):
        raise TypeError("A and B must be integer")
    if A == 0 and B == 0:
        raise ValueError("num1 and num2 can not be zero at the same time")
    if A < 0:
        A = -1 * A
    if B < 0:
        B = -1 * B
    num1 = max(A, B)
    num2 = min(A, B)

    if num2 == 0:
        return num1
   
    divider, remainder = divmod(num1, num2)
    if remainder == 0:
        return num2
    else:
        return getGreatestCommonDivisor(num2, remainder)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
print(getGreatestCommonDivisor(48, -18))
print(gcd(18, 48))