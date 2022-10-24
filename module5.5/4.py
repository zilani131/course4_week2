list1=[10,20,30,40]
list2=[100,200,300,400]
list3=list(zip(list1,reversed(list2)))
print(list3)

for i in list3:
    print(i[0]," ",i[1])