


a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a) # [10, 2, 20, 4, 30, 6, 40, 8, 50]




import random 
fruit=['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)





def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)

"""
[1]
[1, 2]
[1, 2, 3]
"""




a=[1,2,3,4,5]
print(a[3:0:-1]) # [4, 3, 2]