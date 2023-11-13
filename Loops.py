'''there are two types of loops in python programming
loops are used to print the statements repeatedly'''
#while loop
'''Keep asking the user to enter a positive integer until they enter a negative integer:'''
'''num = int(input("Enter a positive integer: "))
while num >= 0:
    print(num)
    num = int(input("Enter another positive integer (or a negative integer to exit): "))
print("Exiting...")'''
'''Print the Fibonacci sequence up to 100 using a while loop:'''
'''a, b = 0, 1
while b <= 100:
    print(b)
    a, b = b, a + b'''
'''program to print 1 to 10 numbers'''
for i in range(1, 11):  #range function
    print(i)
'''list iteration'''
my_list = ['apple', 'banana', 'orange']
for fruit in my_list:
    print(fruit)
'''multiplication of a table by a given number'''
'''num =int(input("enter a number to display the table"))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")'''
