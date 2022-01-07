
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

    def isEmpty(self):
        return True if len(self.list) == 0 else False 

    def push(self, value):
        self.list.append(value)

    


s = Stack()
print(s.isEmpty())
s.push('a')
s.push('b')
print(s)

