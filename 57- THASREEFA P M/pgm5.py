def common_data(myls1, myls2):  
    result=False 
    for x in myls1:  
        for y in myls2:  
             if x == y:  
                 result = True  
                 return result
    return result
X=[52,75,27,31]
Y=[3,10,22,31]
Z=[12,45,67]
    
print(common_data(X,Y))  
print(common_data(X,Z))  

