"""
Q2_power
How to calculate power of a number using recursion?
1. problem: n power of x
2. input: n is int, n >= 0
3. output: float
4. edge case: n = 0, x = 0
5. time complexity
6. space complexity
"""

def power(n: int, x: float) -> float:
    # power(n, x) = x * power(n - 1, x)
    assert n >= 0 and isinstance(n, int), "n must be positive integer or zero"
    if n == 0:
        return 1
    return x * power(n - 1, x)


print(power(n = 4, x = 0))