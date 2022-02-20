
from typing import List 
def merge_sort(lst: List[int]): # by ref time O(NlogN), space O(N)
    if len(lst) <= 1:
        return lst 
    else:
        mid = round(len(lst)/2)
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        i = 0
        j = 0
        ret = list()
        while i < len(lst1) or j < len(lst2):
            if i < len(lst1) and j < len(lst2):
                if lst1[i] < lst2[j]:
                    ret.append(lst1[i])
                    i += 1
                else:
                    ret.append(lst2[j])
                    j += 1
            elif i < len(lst1):
                ret.append(lst1[i])
                i += 1
            else:
                ret.append(lst2[j])
                j += 1
        return ret 





lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
# lst = [3]
a = merge_sort(lst)

print(a)
