from array import *

# 1. Create an array and traverse
print('Step 1:')
arr = array('i', [1, 2, 3, 4, 5])
for v in arr:
    print(v)

# 2. Access individual elements through indexes
print('Step 2:')
print(arr[0])

# 3. Append any value to the array using append() method
print('Step 3:')
arr.append(9)
print(arr)

# 4. Insert value in an array using insert[] method
print('Step 4:')
arr.insert(10, 8) # index, value
print(arr)

# 5. Extend python array using extend() method
print('Step 5:')
arr.extend([10, 20, 30])
print(arr)

# 6. Add items from list into array using fromlist() method
print('Step 6:')
tempList = [200, 201]
arr.fromlist(tempList)
print(arr)

# 7. Remove any array element using remove() method
print('Step 7:')
arr.remove(20) # valueError if not exist, only remove the 1st one
print(arr)

# 8. Remove last array element using pop() method
print('Step 8:')
arr.pop() # remove the last item
arr.pop(0) # remove the first item
print(arr)


# 9. Fetch any element through its index using index() method
print('Step 9:')
print(arr[0]) 

# 10. Reverse a python array using reverse() method
print('Step 10:')
arr.reverse()
print(arr)

# 11. Get array buffer info through buffer_info() method
print('Step 11:')
print(arr.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print('Step 12:')
print(arr.count(10))

# 13. Convert array to string using tostring() method
print('Step 13:')
newArr = arr.tobytes() # .tostring() is not used
print(newArr)

intArr = array('i')
intArr.frombytes(newArr)
print(intArr)

# 14. Convert array to a python list with same elements using tolist() method
print('Step 14:')
print(arr.tolist())


# 15. Append a string to char array using fromstring() method
# .fromstring() is not used

# 16. Slice Elements from an array
print('Step 16:')
print(arr[:3]) # 3 is index, not count


a = [0, 1, 2, 3]
print(a[:3]) # 3 is index, not count

print(a[:]) # print all elements