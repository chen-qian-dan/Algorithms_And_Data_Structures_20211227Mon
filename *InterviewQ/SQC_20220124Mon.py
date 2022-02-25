

# problem definition 
# a = [1, 1.5, 2, 1.7, 3, 4, 3.7, 5] return [2, 4, 5]
# a = [1, 2, 3, 4, 5]                   return [5]      only increasing
# a = [5, 4, 3, 2, 1]                   return [5]      only decreasing 
# a = [5, 5, 5, 4, 3, 2, 1]             return [5]      plateus at the beginning
# a = [1, 2, 3, 4, 4, 4, 5]             return [5]      plateus at the end 
# a = [1, 2, 3, 3, 3, 4, 3, 4, 5]       return [4, 5]   plateus in the middle 
# a = [2, 4, 4, 5]                      return [5]
# a = [2, 4, 4, 4]                      return [4]
# a = [2, 4, 4, 3]                      return [4]
# a = [4, 4, 4]                         return [4] 
# a = [4, 4, 3]                         return [4]
# a = [4]                               return [4] 
# a = []                                return []
# from the example case, I know the last item can be local maxima, how about the first item, can it be local maxima too? 


from typing import List, Union

def get_local_maxima(lst: List[Union[int, float]]) -> List[Union[int, float]]:

    # remove adjacent duplicate number
    tempList = [lst[0]] + [lst[i] for i in range(1, len(lst)) if lst[i] != lst[i-1]] if lst else lst 
    # compare 3 lists item by item
    tempList = [j for i, j, k in zip([tempList[0]] + tempList[:-1], tempList, tempList[1:] + [tempList[-1]]) if j >= i and j >= k] if tempList else tempList
    return tempList


# def get_local_maxima_two(lst: List[Union[int, float]]) -> List[Union[int, float]]:

#     tempList = [lst[0]] + [lst[i] for i in range(1, len(lst)) if lst[i] != lst[i-1]] if lst else lst 
#     tempList = [tempList[0]] + tempList + [tempList[-1]] if tempList else tempList
#     tempList = [tempList[i] for i in range(1, len(tempList) - 1) if tempList[i] > tempList[i - 1] and tempList[i] > tempList[i + 1]] if tempList else tempList

#     return tempList


a = []  

print(get_local_maxima(lst = a))
