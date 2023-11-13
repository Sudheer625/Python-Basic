# by using legb rule we can set the priority for the variables
# l means local e means enclosing g means global b means built in
'''
a=20    # global variable
def display():
    b=10        # local variable
    print("local variable",b)
    print("global variable",a)
display()
print("outside the function",a)
'''
'''
a=10
def display():
    b=20
    print("global variable is",a)
    print("local variable is ",b)
display()
c=40
print("local variable is ",c)
print("global variable is ",a)
'''
'''
# globals method
a=10    # global variable before changing
print(id(a))    # it prints the id of a
def fun2():
    a=9     # local variable
    x=globals()['a']    # checks the global variable
    print(id(x))        # checks if the id matches
    print("in fun2",a)
    globals()['a']=15       # replaces the global variable's value to 15
fun2()
print("outside",a)      # prints replaced value 
'''
'''
# global keyword
greeting="hello"
def change_greeting(new_greeting):
    global greeting
    greeting=new_greeting
def greeting_world():
    world="world"
    print(greeting,world)
change_greeting("hi")
greeting_world()
'''