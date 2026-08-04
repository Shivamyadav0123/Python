#program to check the pass or fail of a student based on marks obtained in three subjects.
Mark1=int(input("Enter Mark1:"))
Mark2=int(input("Enter Mark2:"))
Mark3=int(input("Enter Mark3:"))

Total_persentage= (100*(Mark1+Mark2+Mark3)/300)
if (Total_persentage>=33 and Mark1>=33 and Mark2>=33 and Mark3>=33):
    print("You are Passed",Total_persentage)
else:
    print("You are Failed",Total_persentage)


#print the table.
lst=[2,3,4,5]
tt=map(lambda x:print(f"print the table of {x}") or [print(x,"x",i,"=",x*i) for i in range(1,11)], lst)
list(tt)

#Find the sum of all elements in a list.
#Find the average of all elements in a list.


lst=[10,20,30,40,50,60,70,]
t=sum(lst)
print("The sum of all elements in the list is:", t)

#Find the average of all elements in a list.

lst=[10,20,30,40,50,60,70,]
average=sum(lst)/len(lst)
print("The average of all elements in the list is:", average)

#find the second largest number in a list.
lst=[10,20,30,40,50,60,70]
lst.sort(reverse=True)
print("The second largest number in the list is:", lst[1])

#find the even numbers and odd numbers.
num=int (input("Enter the number"))
if num % 2==0:
    print("even number")
else:
    print("odd number")