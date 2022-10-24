from unittest import result


numbers=[45,40,2,60]
def getNumbers(num):
    for n in num:
        yield n

result=getNumbers(numbers)
print(next(result))
print(next(result))