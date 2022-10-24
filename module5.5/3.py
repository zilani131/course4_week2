


list1=['M',"na","i","Bo"]
list2=["y","me","s","nd","z"]
list3=[]
ma=max(len(list1),len(list2))
print(ma)
for i in range(ma):
    list3.append(list1[i]+list2[i])

print(list3)
