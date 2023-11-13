s={}
print(type(s))  # dictionary and sets are relative to each other
a={1,2,3,4}
print(type(a))  #defining set
a.add('python')
print(a)        # adding elements to set 
a.update(['sudheer'])
print(a)        # modifies the set and adds at last of the set
print(len(a))   #length function used to cxalculate length of the set
b={1,2.2,'python programming',1}
print(b)        # it takes only one unique value
print(type(b))
b.remove(2.2)   # remove function uses to remove set elements
print(b)
 #set relations
s1={1,2,3,4,5,6}
s2={7,8,9,10}
print(s1.union(s2)) # union relation uses to combine the two sets(adding)
print(s1.intersection(s2))  # intersection relation uses to display the same elements in the set
print(s1.difference(s2))    # differnece relation shows the different elements in the set
print(s1.isdisjoint(s2))    # disjoint relation shows if sets having different elements