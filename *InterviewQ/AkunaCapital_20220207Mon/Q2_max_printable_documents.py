
from typing import List 

def max_printable_documents(documents: List[int], is_malfunctioning: List[bool], x: int) -> int:
    # Write your code here
    # sliding window
    if len(documents) == 0:
        return 0
    if x >= len(documents):
        return sum(documents)
    
    maxDoc = 0
    for i in range(x, len(documents)):
        if is_malfunctioning[i] == 0:
            maxDoc += documents[i]
    for i in range(0, x):
        maxDoc += documents[i]
        
    ret = maxDoc
    for i in range(x, len(documents)):
        newMaxDoc = maxDoc
        if is_malfunctioning[i] == 1:
            newMaxDoc += documents[i]
        if is_malfunctioning[i - x] == 1:
            newMaxDoc -= documents[i - x]
        maxDoc = newMaxDoc
        ret = max(ret, newMaxDoc)
        
    return ret 


# documents =         [5,0,1,3,1,6,2]
# is_malfunctioning = [0,1,1,0,0,1,0]
# x = 2

# print(max_printable_documents(documents, is_malfunctioning, x)) # 17

documents =         [1,0,4,2,0,3]
is_malfunctioning = [1,0,1,0,1,0]
x = 3

print(max_printable_documents(documents, is_malfunctioning, x)) # 10
