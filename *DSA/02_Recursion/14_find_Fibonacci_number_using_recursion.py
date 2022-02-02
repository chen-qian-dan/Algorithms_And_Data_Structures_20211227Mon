"""
f(n) = f(n-1) + f(n-2)
"""

def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n >= 0 must be true")
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4)) # 3