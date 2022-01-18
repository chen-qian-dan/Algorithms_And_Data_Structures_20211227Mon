# Activity Selection Problem


activities = [["A1", 0, 6], 
            ["A2", 3, 4], 
            ["A3", 1, 2], 
            ["A4", 5, 8], 
            ["A5", 5, 7], 
            ["A6", 8, 9]]



def printMaxActivities(activities): # -------- time O(NlogN), space O(1)
    # sort activities based on finished time
    activities.sort(key = lambda x: x[2]) # -------- time O(NlogN)
    lastSelectedActivityFinishedTime = None 
    for i, v in enumerate(activities):# -------- time O(N)
        if i == 0:
            lastSelectedActivityFinishedTime = v[2]
            print(v)
        else:
            if v[1] >= lastSelectedActivityFinishedTime:
                print(v)
                lastSelectedActivityFinishedTime = v[2]


printMaxActivities(activities)



