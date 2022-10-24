""""
marks=[30,20,10,100]
total=sum(marks)
print(total)
ctn=0
for mark in marks:
    ctn+=mark

print(ctn)


marks={30,20,10,100}
total=sum(marks)
print(total)
ctn=0
for mark in marks:
    ctn+=mark

print(ctn)
marks=30,20,10,100
total=sum(marks)
print(total)
ctn=0
for mark in marks:
    ctn+=mark

print(ctn)"""
marks={'pysics':40,'english':30}
total=0
for value in marks.values():
    total+=value
print(total)
t=0
for mark in marks:
    value=marks[mark]
    t+=value
print(total)
for a,b in marks.items():
    print(a,b)
for i,b in enumerate(marks):
    print(i,b)

