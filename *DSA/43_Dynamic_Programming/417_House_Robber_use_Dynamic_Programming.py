
def house_robber_top_down(houses, index, dp):
    if index >= len(houses):
        return 0
    if index not in dp.keys():
        sub1 = houses[index] + house_robber_top_down(houses, index + 2, dp)
        sub2 = house_robber_top_down(houses, index + 1, dp)
        dp[index] = max(sub1, sub2)
    return dp[index]


def house_robber_bottom_up(houses):
    tb = [0] * len(houses) # or do tb = [0] * (len(houses)+2)
    tb[-1] = houses[-1]
    tb[-2] = max(houses[-1], houses[-2])
    for i in range(len(houses)-3, -1, -1):
        tb[i] = max(houses[i] + tb[i+2], tb[i+1])

    return tb[0]


dp = dict()
houses = [6, 7, 1, 30, 8, 2, 4] # expect 41
print(house_robber_top_down(houses, 0, dp))
print(house_robber_bottom_up(houses))