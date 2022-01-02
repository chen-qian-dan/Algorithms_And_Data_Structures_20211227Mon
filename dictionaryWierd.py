a = {(1,2):1,(2,3):2}
print(a[(1,2)])


a = {(1,2):1,(2,3):2}
print(a[1,2])


rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)