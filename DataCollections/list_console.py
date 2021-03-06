Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [4,3,5,6,'hi',10.55,True]
>>> type(data)
<class 'list'>
>>> data[0]
4
>>> data[0:3]
[4, 3, 5]
>>> data[-1]
True
>>> data = []
>>> data.append(40)
>>> data
[40]
>>> data.append(10)
>>> data
[40, 10]
>>> data.append(30)
>>> data
[40, 10, 30]
>>> data.append(43,21,22,68,21)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.append(43,21,22,68,21)
TypeError: append() takes exactly one argument (5 given)
>>> data.append([43,21,22,68,21])
>>> data
[40, 10, 30, [43, 21, 22, 68, 21]]
\
>>> data[-1]
[43, 21, 22, 68, 21]
>>> data.pop()
[43, 21, 22, 68, 21]
>>> data.extend([43,21,22,68,21])
>>> data
[40, 10, 30, 43, 21, 22, 68, 21]
>>> data.pop(4)
21
>>> data
[40, 10, 30, 43, 22, 68, 21]
>>> data.index(43)
3
>>> data.pop(3)
43
>>> data
[40, 10, 30, 22, 68, 21]
>>> data.insert(3,43)
>>> data
[40, 10, 30, 43, 22, 68, 21]
>>> data.remove(6)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data.remove(6)
ValueError: list.remove(x): x not in list
>>> data.remove(10)
>>> data
[40, 30, 43, 22, 68, 21]
>>> sorted(data)
[21, 22, 30, 40, 43, 68]
>>> sorted(data,reverse=True)
[68, 43, 40, 30, 22, 21]
>>> data
[40, 30, 43, 22, 68, 21]
>>> data.sort()
>>> data
[21, 22, 30, 40, 43, 68]
>>> data.sort()
>>> sorted(data)
[21, 22, 30, 40, 43, 68]
>>> data = []
>>> for i in range(50):
	data.append(i)

	
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> data = [i for i in range(50)]
>>> data
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> data = [i for i in range(50) if i % 2 == 0]
>>> data
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data[0] =45
>>> data
[45, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data[0:4] = 4
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data[0:4] = 4
TypeError: can only assign an iterable
>>> data[0:4] = [4,5]
>>> data
[4, 5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> a = data
>>> a == data
True
>>> a is data
True
>>> a
[4, 5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data
[4, 5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> del a[0]
>>> a
[5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data
[5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data
[5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data[:]
[5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> b = data[:]
>>> b == data
True
>>> b is data
False
>>> data[0] = 12
>>> data
[12, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> b
[5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> data = [2,3,5,5,1,[21,22,34,65,11]]
>>> c = data[:]
>>> c == data
True
>>> c is data
False
>>> c[0] = 100
>>> c
[100, 3, 5, 5, 1, [21, 22, 34, 65, 11]]
>>> data
[2, 3, 5, 5, 1, [21, 22, 34, 65, 11]]
>>> c[-1]
[21, 22, 34, 65, 11]
>>> c[-1][0] = 100
>>> c
[100, 3, 5, 5, 1, [100, 22, 34, 65, 11]]
>>> data
[2, 3, 5, 5, 1, [100, 22, 34, 65, 11]]
>>> import copy
>>> d = copy.deepcopy(data)
>>> d
[2, 3, 5, 5, 1, [100, 22, 34, 65, 11]]
>>> data
[2, 3, 5, 5, 1, [100, 22, 34, 65, 11]]
>>> data[-1][0] = 0
>>> data
[2, 3, 5, 5, 1, [0, 22, 34, 65, 11]]
>>> d
[2, 3, 5, 5, 1, [100, 22, 34, 65, 11]]
>>> 
