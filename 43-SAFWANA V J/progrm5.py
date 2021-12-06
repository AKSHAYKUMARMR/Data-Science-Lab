def common_data(mylist1,mylist2):  
    result=False 
    for x in mylist1:  
        for y in mylist2:  
             if x == y:  
                 result = True  
                 return result
    return result
A=[7,8,9,10,11]
B=[12,13,14,15,16]
C=[11,7,10,9]
    
print(common_data(A,B))  
print(common_data(A,C))  

