'''functions is a block of statement it is used to perform specific tasks
uses of functions
code reduceability
code complexicity
memory allocation
Syntax: def functionname():
        stmts
        
functionname()  #function calling
def keyword is used to create a function'''
# defining a function
def sudheer(a, b):  #creating a function with two arguments
    print(a, b)
sudheer(1, 2)  # call the function with arguments 1 and 2
def sudheer(a):
    print(a)
sudheer(12)     # holds only single argument
#arbitary argument
def sudheer(*a):    #creates a tuple
    print(a)
sudheer(1,2,3,4,5)  # holds multiple values
#keyword argument
def sudheer(**a):   # creates a dict
    print(a)
sudheer(name="sudheer",age=18)  # holds keys and values 
# function calling
def functionname():
    print("this is function")
functionname()
# arguments passing
def functionname(name):
    print("hello",name)
functionname("sudheer")
# multuple arguments
def functionname(name,age):
    print("function block excecuted",name,age)
functionname('sudheer',18)
# return statement
def function1(a,b):
    return a+b
w=function1(60,40)
print(w)
# example for return stmt 2
def fun2(a):
    return a*3
print(fun2(30))
# looping in functions
def fun3(a):
    for i in a:
        print(i)
fun3([1,2,3,4,5,6,7,8,9])