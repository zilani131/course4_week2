from audioop import reverse


num=[30,20,30,-29]
print(sorted(num,reverse=True))
actors=[

    {'name':'zilani','age':20},
    {'name':'sadik','age':18},
    {'name':'sadi','age':28},
]
sorted_actor=sorted(actors,key=lambda actor :actor['age'])
print(sorted_actor)