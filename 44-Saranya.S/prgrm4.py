def Merge(dict1,dict2):
    return(dict2.update(dict1))
dict1={'a':10,'b':8}
dict2={'c':4,'d':5}
print(Merge(dict1,dict2))
print(dict2)
