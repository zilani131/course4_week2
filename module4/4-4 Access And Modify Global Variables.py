from unittest import result


balance=400
def globalVarible(num1,num2):
    global balance
    result=num1+num2
    balance=result
    print(result)


globalVarible(4,5)
print(balance)