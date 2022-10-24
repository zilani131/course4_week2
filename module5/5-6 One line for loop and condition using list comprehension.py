numbers=[2,3,5,10,30,15]
odd_number=[]
for num in numbers:
    if num%2==1:
        odd_number.append(num)
    

print(odd_number)

odd_number2=[num for num in numbers if num%2==1]
print(odd_number2)
names=['zilani','sami']
ages=[30,50]
pairs=[ [name,age] for name in names for age in ages if age>30]
print(pairs)