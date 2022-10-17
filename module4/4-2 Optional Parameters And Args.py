from unittest import result


def mul(num1,num2=2):
    mul=num1*num2
    print(num1,num2)
    return mul
z=mul(45)
print(z)
s=mul(num2=30,num1=10)
print(s)
def multiply(*numbers):
    print(numbers)
    result=1
    for num in numbers:
        result=result*num
    return result
finalMul=multiply(1,2,3,5)
print(finalMul)