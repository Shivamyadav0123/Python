#Create a list of 10 numbers and print all elements.
#Find the largest element in a list without using max().
#Find the smallest element in a list without using min().
#Find the sum of all elements in a list.
#Find the average of all elements in a list.
#Remove duplicate elements from a list.
#Reverse a list without using reverse().
#Find the second largest element in a list.


num=[10,20,30,40,50,60,70,80,90,95]
for i in num:
   print(i)

num=[10,20,30,40,50,60,70,80,90,95]
largest=num[0]
for i in num:
    if i>largest:
        largest=i
print("Largest element:", largest)


num=[10,20,30,40,50,60,70,80,90,95]
smallest=num[0] 
for i in num:
    if i<smallest:
        smallest=i
print("Smallest element:", smallest)


num=[10,20,30,40,50,60,70,80,90,95]
sum=0
for i in num:
    sum+=i
print("Sum of all elements:", sum)


num=[10,20,30,40,50,60,70,80,90,95]
average=sum(num)/len(num)
print("Average of all elements:", average)


num=[10,20,30,40,50,60,70,80,90,95,50,60,70]
remove_duplicates = []
for i in num:
    if i not in remove_duplicates:
        remove_duplicates.append(i)
print("List after removing duplicates:", remove_duplicates)


num=[10,20,30,40,50,60,70,80,90,95]
reversed_list = []
for i in range(len(num)-1, -1, -1):
    reversed_list.append(num[i])
print("Reversed list:", reversed_list)


num=[10,20,30,40,50,60,70,80,90,95]
second_largest = None
largest = num[0]
for i in num:
    if i > largest:
        second_largest = largest
        largest = i
    elif second_largest is None or (i > second_largest and i < largest):
        second_largest = i

print("Second largest element:", second_largest)


#Set
#Create a set and print all elements.
#Find the union of two sets.
#Find the intersection of two sets.
#Find the difference between two sets.
#Remove duplicate values from a list using a set.

a={10,20,30,40,50,60,70,80,90,95}
for i in a:
    print(i)


a={10,20,30,40,50,60,70,80,90,95}
b={50,60,70,80,90,100,110,120}
union_set = a.union(b)
print("Union of two sets:", union_set)

a={10,20,30,40,50,60,70,80,90,95}
b={50,60,70,80,90,100,110,120}
intersection_set = a.intersection(b)
print("Intersection of two sets:", intersection_set)

a={10,20,30,40,50,60,70,80,90,95}
b={50,60,70,80,90,100,110,120}
difference_set = a.difference(b)
print("Difference between two sets:", difference_set)

a={10,20,30,40,50,60,70,80,90,95}
b=(50,60,70,80,90,100,110,120)
duplicate_removed_list = list(set(list(a) + list(b)))
print("List after removing duplicates using set:", duplicate_removed_list)