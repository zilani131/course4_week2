sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
sample={k : v for (k,v ) in sample_dict.items() if k=="name" or k=="age"}
print(sample)