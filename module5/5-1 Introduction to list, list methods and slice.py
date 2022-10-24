numbers=[]

for i in range(0,7):
   numbers.append(int(input()))
print(numbers[:])

numbers.insert(1,5)
numbers.pop(4)
for i in range(0,len(numbers)):
    print(numbers[i])
