sample_dict = {'a': 100, 'b': 200, 'c': 300}
v1=0
for (k,v) in sample_dict.items():
    if(v==100):

        v1=1
        break


if(v1):
    print("Present")
else:
    print("Not present")
    