"""
Divide and conquer:
397- Zero One Knapsack
- Given the weights and profits of N items
- Find the maximum profit within given capacity of C
- Items cannot be broken 

1. problem: can't repeat items
2. input: [(weight, profit)], C
3. output: int
4. edge: 
5. time
6. space 
"""


def zero_one_snapsack(items, C, index: int) -> int:
    if index >= len(items) or index < 0:
        return 0
    if C <= 0:
        return 0
    if C < items[index][0]:
        return zero_one_snapsack(items, C, index + 1)

    # pick
    sub1 = items[index][1] + zero_one_snapsack(items, C - items[index][0], index + 1)

    # don't pick
    sub2 = zero_one_snapsack(items, C, index + 1)

    return max(sub1, sub2)


lst = [(3, 31), (1, 26), (2, 17), (5, 72)]
C = 7

print(zero_one_snapsack(lst, C, 0))