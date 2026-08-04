"""file Hanling in python 
File handling in python allow you to read from and write to files.This 
is important when you want to store data permanently or work with 
large datasets.
python provides build-in function and methods to interact with File."""

"""steps for file handling in python:
1.Opening a file
2.Reading from a file
3.Writing to a file
4.Closing a file"""


#Open a file:

file_object = open("filename", "mode")

#mode: "r" - read mode, "w" - write mode, "a" - append mode, "rb" - read binary mode, "wb" - write binary mode.
 
file=open("example.txt", "r")  # Open a file in read mode
#Reading from a file:
#file me sabhi content read karne ke liye read() method ka use karte hai.

file=open("example.txt", "r")  # Open a file in read mode
content = file.read()  # Read the entire content of the file
print(content)  # Print the content
file.close()  # Close the file

#readline() method ka use karte hai file me se ek line read karne ke liye.

file=open("example.txt", "r")  # Open a file in read mode
line=file.readline()  # Read the first line of the file
print(line)  # Print the first line
file.close()  # Close the file

#readlines() method ka use karte hai file me se sabhi lines read karne ke liye.
#reads all lines into a list.

file=open("example.txt", "r")  # Open a file in read mode
lines=file.readlines()  # Read all lines of the file
print(lines)  # Print all lines
file.close()  # Close the file

#Writing to a file:
#file me content write karne ke liye write() method ka use karte hai.
file=open("example.txt", "w")  # Open a file in write mode
file.write("Hello, World!")  # Write content to the file
file.close()  # Close the file

#Appending to a file:
#file me content append karne ke liye append() method ka use karte hai.
file=open("example.txt", "a")  # Open a file in append mode
file.write("This is a new line.")  # Append content to the file
file.close()  # Close the file