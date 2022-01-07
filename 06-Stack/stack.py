
import copy 

# create stack using list without size limit
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        tmpList = copy.deepcopy(self.list)
        tmpList.reverse()
        values = [str(x) for x in tmpList]
        return '\n'.join(values)

    


s = Stack()
print(s)

