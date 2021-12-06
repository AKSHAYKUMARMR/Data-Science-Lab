mylist=[2,7,1,4,2,6,7]
print(mylist)
s=[]
for i in mylist:
    if i not in s:
        s.append(i)
print(s)        
        
