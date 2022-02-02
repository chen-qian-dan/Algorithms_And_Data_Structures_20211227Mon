
def getGreatestCommonDivisor(x: int, y: int) -> int:
    if x == 0 or y == 0:
        raise ValueError("None of x or y can be zero")
    if x == 1 or y == 1:
        return 1
    if x == y:
        return x

    if x < 0:
        x = -1 * x
    if y < 0:
        y = -1 * y

    big = max(x, y)
    small = min(x, y)

    carrier, remain = divmod(big, small)
    if remain == 0:
        return small
    return getGreatestCommonDivisor(small, remain)


print(getGreatestCommonDivisor(45, 10)) # 5