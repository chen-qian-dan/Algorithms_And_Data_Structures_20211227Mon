def powerOfTwoRecursion(n: int):
    if n < 0:
        raise ValueError("n can not < 0")
    if n == 0:
        return 1
    return 2 * powerOfTwoRecursion(n - 1)


def powerOfTwoIteration(n: int):
    if n < 0:
        raise ValueError("n can not < 0")
    power = 1
    for i in range(n):
        power *= 2
    return power 

val = 0
a = powerOfTwoRecursion(val)
print(a)

a = powerOfTwoIteration(val)
print(a)


val = 1
a = powerOfTwoRecursion(val)
print(a)

a = powerOfTwoIteration(val)
print(a)

