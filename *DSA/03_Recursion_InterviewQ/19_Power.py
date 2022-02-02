"""
How to calculate power of a number using recursion?
1. problem: n power of x
2. input: n is int, n >= 0
3. output: float
4. edge case: n = 0, x = 0
5. time complexity
6. space complexity
"""

def power(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if x in [0.0, 1.0]:
        return x
    
    return x * power(x, n - 1)



print(power(x = 2, n = 4)) # 16
    