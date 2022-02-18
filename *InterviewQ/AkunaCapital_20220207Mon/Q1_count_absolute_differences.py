from typing import List

def count_absolute_differences(l: List[int], x: int) -> int:
    # Write your code here
    if len(l) <= 1:
        return 0
    
    count = set()
    visited = dict()
    for i, v in enumerate(l):
        gap1 = (v - x)
        gap2 = v + x
        if gap1 in visited.keys(): 
            left = min(gap1, v)
            right = max(gap1, v)
            count.add((left, right))
            
        if gap2 in visited.keys():  # not elif
            left = min(gap2, v)
            right = max(gap2, v)
            count.add((left, right))
            
        visited[v] = i
        
    return len(count) 


l = [5,2,6,3,3]
x = 3

print(count_absolute_differences(l, x))