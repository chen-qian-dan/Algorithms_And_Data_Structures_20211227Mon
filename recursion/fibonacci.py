# fibonacci

def fibonacci(n: int) -> int:
    assert n >= 0 and isinstance(n, int), "n must be positive integer"
   
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))