
# stack with limit size 

import copy 

# create 
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        tmpList = copy.deepcopy(self.list)
        tmpList.reverse()
        values = [str(x) for x in tmpList]
        return '\n'.join(values)

    def push(self, value):
        if len(self.list) < self.maxSize:
            self.list.append(value)
        else:
            print("Can't push, exceed the max size")



s = Stack(10)
s.push(1)
s.push(2)
print(s)
print("-------------")
print(s)

