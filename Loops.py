#Loops
#1. Print numbers from 1 to 100 using a loop.
#2. Print all even numbers from 1 to 100.
#3. Find the sum of all elements in an array using a loop.
#4. Find the largest element in an array.
#5. Count the number of positive and negative numbers in an array.

#1. Print numbers from 1 to 100 using a loop.
"""for i in range(1, 101):
    print(i)


for i in range(1,101):
    if i % 2 == 0:
        print(i) 


arr = [20,30,40,50,60,70,80,90,100]
sum=0
for i in arr:
    sum+=i
print("Sum of all elements in the array:", sum)


arr = [20, 30, 40, 50, 60, 70, 80, 90, 100]
#4. Find the largest element in an array.
largest = arr[0]
for i in arr:
    if i>largest:
        largest=i

print("Largest element in the array:", largest)


arr=[-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]
#5. Count the number of positive and negative numbers in an array.
positive_count=0
negative_count=0
for i in arr:
    if i>0:
        positive_count+=1
    elif i<0:
        negative_count+=1

print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)


#Arrays & Strings
#29. Reverse a string.
#30. Check whether a string is a palindrome.

str = ("Hello World")
reverse_str = ""
for i in str:
    reverse_str = i + reverse_str

print("Reversed string:", reverse_str)


str = "madam"
reverse_str = ""
for i in str:
    reverse_str = i + reverse_str

if str == reverse_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")"""


a=[2,3,4,5,6,7,8,9,10,11,12,]
even_count=0
for i in a:
    if i%2==0:
        even_count+=1
print("Number of even numbers:", even_count)


