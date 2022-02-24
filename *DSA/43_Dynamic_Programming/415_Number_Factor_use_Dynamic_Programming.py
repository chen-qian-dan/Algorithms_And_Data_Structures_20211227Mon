"""
Given N, find the number of ways to express N as a sum of 1, 3, 4
"""

"""
0 : 0
1 : 1
N : N-1, N-3, N-4
"""
def numberFactor_topDown(N, dp):
    if N in [0, 1, 2]:
        return 1
    elif N == 3:
        return 2
    if N not in dp.keys():
        dp[N] = numberFactor_topDown(N-1, dp) + numberFactor_topDown(N-3, dp) + numberFactor_topDown(N-4, dp)
    return dp[N]



def numberFactor_bottomUp(N):
    if N <= 0:
        return 0
    tb = [1, 1, 1, 2]
    for i in range(4, N+1):
        tb.append(tb[i-1] + tb[i-3] + tb[i-4])
    return tb[N]


dp = dict()
N = 5 # expect 6
print(numberFactor_topDown(N, dp))

print(numberFactor_bottomUp(N))