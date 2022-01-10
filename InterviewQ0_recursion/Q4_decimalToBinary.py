# Q4_decimalToBinary
"""
Convert a number from Decimal to Binary using recursion
1. problem:
    2 -> 10
2. input: int
3. output: str
4. edge cases:
    -2 -> ? 
5. time complexity
6. space complexity

dividor, remainder = divmod(4, 2)
f(4) = f(dividor)*10 + (remainder)
"""

def decimalToBinary(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n == 0:
        return 0
    if n < 0:
        n = -1 * n

    dividor, remainder = divmod(n, 2) # be careful: divmod(-7, 2) = -4, 1
    return decimalToBinary(dividor) * 10 + remainder 


def decimalToBinaryVideo(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinaryVideo(int(n/2))

print(decimalToBinary(-13))