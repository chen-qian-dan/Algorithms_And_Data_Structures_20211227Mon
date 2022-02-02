"""
How to find the sum of digits of a positive integer number using recursion?
1. problem 
2. intput: int
3. output: int 
4. edge cases
5. time complexity
6. space complexity
"""

def sumOfDigits(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive integer")

    newN, remainder = divmod(n, 10)
    if newN > 0:
        return remainder + sumOfDigits(newN)
    else:
        return remainder


print(sumOfDigits(4401))