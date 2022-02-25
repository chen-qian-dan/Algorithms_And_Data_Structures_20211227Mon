


def snapsack_top_down(lst, index, C, dp):
    if index >= len(lst):
        return 0
    if C <= 0:
        return 0
    if not (index, C) in dp.keys():
        if lst[index][0] < C:
            sub1 = snapsack_top_down(lst, index + 1, C, dp)
            sub2 = lst[index][1] + snapsack_top_down(lst, index + 1, C - lst[index][0], dp)
            dp[(index, C)] = max(sub1, sub2)
        else:
            dp[(index, C)] = snapsack_top_down(lst, index + 1, C, dp)

    return dp[(index, C)]



lst = [(3, 31), (1, 26), (2, 17), (5, 72)]
C = 7

dp = dict()
print(snapsack_top_down(lst, 0, C, dp))  # expect 98