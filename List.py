'''list is a user defined datatype it can stores different datatyped elements in a single format 
list is a mutable datatype'''
a=[]
print(type(a))
a.append(1)     #append function
print(a)
a.extend([2,3,4,5,30,23,11,44])     #extend function
print(a)
a.insert(5,"sudheer python programming")    #insert function
print(a)
print(len(a))   #length function 
a.pop(2)
print(a)
for i in a:
    print(i)    #list elements looping
sudheer=[1,1,2.24,'sudheer',False]
sudheer.pop(1)  # pop function
print(sudheer)  
print(sudheer.count(3))
s1=[1,1,2.24,4,6,7,98,7]
s1.sort()   # sort function 
print(s1)
s2=[2,2,3.34,[4,6,7,98],7]  # nested list 
print(s2[3][0])