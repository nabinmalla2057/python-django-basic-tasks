list=[1,-2,3,14,-9,6,-20]
#print(list)
for i in list:
    if i<0:
        list.remove(i)
print(list)