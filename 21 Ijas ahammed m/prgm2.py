a=[]
n = int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int( input("Enter element:"))
    a.append(b)
a = list(dict.fromkeys(a))
print(a)
    
