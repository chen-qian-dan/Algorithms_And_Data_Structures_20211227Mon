activities = [["A1", 0, 6], 
            ["A2", 3, 4], 
            ["A3", 1, 2], 
            ["A4", 5, 8], 
            ["A5", 5, 7], 
            ["A6", 8, 9]]


def getMaxActivities(activities): # time O(NlogN + N) space O(1)
    # sort activities based on end time 
    activities.sort(key = lambda x: x[2]) # time O(NlogN)
    ret = list()
    ret.append(activities[0]) 
    for i in range(1, len(activities)): # time O(N)
        act = activities[i]
        # check if the start time of act after the end time of ret
        if act[1] >= ret[-1][2]:
            ret.append(act)

    return ret 

print(getMaxActivities(activities))


    