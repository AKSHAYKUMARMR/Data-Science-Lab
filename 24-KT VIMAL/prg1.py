mylist=[2,3,4,5,6]
print(mylist)
j=mylist[0]
for i in mylist:
    if i>j:
        j=i
print("Largest number is",j)
