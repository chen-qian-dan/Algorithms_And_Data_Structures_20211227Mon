
# Recursion: Factorial

import sys
sys.setrecursionlimit(100)



def factorial(n: int) -> int:
    # assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n < 0 or not isinstance(n, int):
        raise ValueError("The number must be positive integer only")
        
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)  # recursive case 


print(factorial(-3))