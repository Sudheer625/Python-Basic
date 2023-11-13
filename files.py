# Open the file in write mode and store the file object in f1
f1 = open("hello.txt", "w")
# Write the string to the file
f1.write("Welcome to Sudheer's Python programming.")
# Close the file to ensure changes are saved
f1.close()
f1= open("hello.txt", "r")
print(f1.read())