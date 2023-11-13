'''it is a user defined datatype'''
dict = {"name": "sudheer"}  #initilization of dict
print(dict)                 # printing dict values
print(type(dict))
print(dict["name"])         # acessing values
'''here name is called as key and sudheer is called value'''
dict1={"name":"sudheer","phno":223345}
print(dict1)    # prints keys and values in dict
print(type(dict1))
dict2={"name":"sudheer","rollno":"22mt1a0583"}
print(dict2["name"])    #acessing key1
print(dict2["rollno"])  #acessing key2
dict2.pop("rollno")     # pop method is used to remove particular keys and  values
print(dict2)
dict2.update({"adress":"srikakulam,532001"})    # update method is used to modify the keys and values in existing dict
print(dict2)
dict2.clear()   # clear method is used to clear the keys and values in exsisting dict
print(dict2)
