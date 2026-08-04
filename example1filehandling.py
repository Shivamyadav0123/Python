#open file:
file=open("example.txt", "r")

#read file:
file=open("example.txt", "r")
content=file.read()
print(content)
file.close()

#read line:
file=open("example.txt", "r")
line=file.readline()
print(line)
file.close()

#read lines: give me all lines in list format.
file=open("example.txt", "r")
lines=file.readlines()
print(lines)
file.close()

#write file:
file=open("example1.txt", "w")
file.write("My name is shivam yadav!")
file.close()

#append file:
file=open("example1.txt", "a")
file.write("I am from Hardoi!")
file.close()


#close a file:
#using a statement.
with open("example1.txt", "r") as file:
    content = file.read()
    print(content)