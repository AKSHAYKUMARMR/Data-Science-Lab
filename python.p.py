Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=[10,55,9,23]
>>> print("largest number is:",max(num))
largest number is: 55
>>> num=[1,2,3,3,2,1]
>>> print(list(set(num)))
[1, 2, 3]
>>> tuple=((1,"a"),(2,"b"))
>>> dictionary=dict(tuple)
>>> print(dictionary)
{1: 'a', 2: 'b'}
>>> dict1={'a':1,'b':2}
>>> dict2={'c':4,'d':5}
>>> print(merge(dict1,dict2))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(merge(dict1,dict2))
NameError: name 'merge' is not defined
>>> dict1={'a':1,'b':2}
>>> dict2={'c':4,'d':5}
>>> dict3=merge(dict1,dict2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict3=merge(dict1,dict2)
NameError: name 'merge' is not defined
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 