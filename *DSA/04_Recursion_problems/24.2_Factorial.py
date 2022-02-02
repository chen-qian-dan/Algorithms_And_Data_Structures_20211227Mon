
def factorial(num: int) -> int:
    if num in [0, 1]:
        return 1
    return num * factorial(num - 1)