result=lambda x :x*2
print(result(2))
z=2,3,4,5
x=set(map(result,z))
print(x)
re=list(filter(lambda x:x>2,z))
print(re)
t=[
    {'name':'zilani','age':40},
    {'name':'zil','age':43},
    {'name':'zili','age':440},
    {'name':'lani','age':430}
    
    ]
rx=list(filter(lambda person:person['age']>40,t))
print(rx)