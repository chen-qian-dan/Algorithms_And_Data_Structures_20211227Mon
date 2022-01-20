"""
Divide and Conquer:
Fibonacci Series
A series of numbers in which each number is the sum of the 2 preceding numbers. 
First 2 numbers by definition are 0 and 1
exam:
0, 1, 1, 2, 3, 4, 7, ...
Fib(n) = Fib(n-1) + Fib(n-2)
"""

def fib(n: int) -> int:
    if n < 1:
        raise ValueError("Wrong input")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(6))