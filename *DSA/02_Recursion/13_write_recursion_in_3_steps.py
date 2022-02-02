"""
Factorial
0! = 1
4! = 4 * 3 * 2 * 1

step 1: recursion case
n! = n * (n - 1)!

step 2: Base case - the stopping criterion 
step 3: Unintentional case - the constraint
factorial(-1) ?
factorial(1.5) ?
n >= 0
n is int
"""

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n >= 0 must be True")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
         