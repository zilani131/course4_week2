def num(**numbers):
    print(numbers)
    for keys,value in numbers.items():
        print(keys,value)
num(num1=5,num2=6,num3=10)
def numT(first,*num1,**num2):
    print(first)
    print(num1)
    print(num2)
numT(3,4,5,f=6,s=7)