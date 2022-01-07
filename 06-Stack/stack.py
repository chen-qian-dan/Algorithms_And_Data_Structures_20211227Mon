
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

    def pop(self):
        if len(self.list) == 0:
            return "The stack is empty"
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        return self.list[-1]



s = Stack()
print(s.isEmpty())
s.push('a')
s.push('b')
print(s)
# print("pop ---------------------------")
# print(s.pop())
# print(s)
print("peek ---------------------------")
print(s.peek())

