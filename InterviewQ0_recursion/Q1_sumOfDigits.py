# Q1_sumOfDigits
"""
How to find the sum of digits of a positive integer number using recursion?
1. problem 
2. intput: int
3. output: int 
4. edge cases
5. time complexity
6. space complexity
"""
def sumOfDigits(num: int) -> int:
    assert num >= 0 and isinstance(num, int), "num must be a positive integer"
    if num == 0:
        return 0
    divider, remainder = divmod(num, 10)
    return remainder + sumOfDigits(divider)

print(sumOfDigits(200))
    