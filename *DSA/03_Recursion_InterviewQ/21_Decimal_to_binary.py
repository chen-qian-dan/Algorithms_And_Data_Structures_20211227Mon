"""
Convert a number from Decimal to Binary using recursion 

1. problem
2. input
3. output
4. edge case
5. time complexity
6. space complexity
"""

def decimalToBinary(n: int) -> str:
    # n < 0 ?

    if n in [0, 1]:
        return str(n)

    carrier, remain = divmod(n, 2)
    if carrier == 0:
        return str(remain) 
    return decimalToBinary(carrier) + str(remain)


print(decimalToBinary(1))