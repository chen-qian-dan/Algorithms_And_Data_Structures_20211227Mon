
from typing import List
import math

def bucket_sort(lst: List[int]) -> List[int]: # by ref time O(N^2), if use quick sort O(NlogN), space O(N)
    size = len(lst)
    if size <= 1:
       return lst # by val
    else:
        # hashing func
        bucketCount = round(math.sqrt(size))
        maxVal = max(lst)

        # create buckets
        buckets = [[] for _ in range((bucketCount + 1))]
        # buckets = [[]* 4] # wrong, output is [[]]

        # hashing
        for v in lst:
            index = math.ceil(v * bucketCount / maxVal)
            buckets[index].append(v)

        # sort bucket
        for bucket in buckets:
            bubble_sort(bucket)

        # mergy bucket directly
        ret = list()
        for bucket in buckets:
            ret.extend(bucket)
    return ret 



        
def bubble_sort(lst: List[int]): # by ref
    if len(lst) <= 1:
        pass 
    for j in range(len(lst) - 1, -1, -1):
        for i in range(0, j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]



lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
# lst = [3]
ret = bucket_sort(lst)
print(lst)
print(ret)
