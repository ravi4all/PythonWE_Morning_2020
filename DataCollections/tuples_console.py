Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = 10,21,2,5,6,3
>>> x = (10,21,2,5,6,3)
>>> x[0]
10
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name,age,sal = 'Ram',43,123433
>>> data
('Ram', 43, 123433)
>>> name
'Ram'
>>> age
43
>>> sal
123433
>>> data = (i for i in range(1,10))
>>> data
<generator object <genexpr> at 0x00000202DD503C00>
>>> for i in data:
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> type(data)
<class 'generator'>
>>> next(data)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    next(data)
StopIteration
>>> data = (i for i in range(1,10))
>>> next(data)
1
>>> next(data)
2
>>> next(data)
3
>>> 
