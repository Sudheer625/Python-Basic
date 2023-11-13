f1 = open("mlines.txt", "w")
lines = ["welcome\n", "python\n", "programming\n"]
f1.writelines(lines)
f1.close()
f1 = open("mlines.txt", "r")
print(f1.readline())
print(f1.readline())
print(f1.readline())
