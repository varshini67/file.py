data1 = input("data1:")
data2 = input("data2:")
dict1=dict(Zip(list1,list2))
key = input('key:')
if key in dict1:
  print("value:",dict1.pop(key))
  sorted_dict = sorted(dict1.items())
  print("dictonary: ",sorted_dict)
else:
  print("Key does not exist")
  

