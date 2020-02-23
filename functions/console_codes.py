Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello():
	msg = "Hello User"
	print(msg)

	
>>> hello()
Hello User
>>> m = hello()
Hello User
>>> print(m)
None
>>> def hello():
	msg = "Hello User"
	return msg

>>> hello()
'Hello User'
>>> m = hello()
>>> print(m)
Hello User
>>> print(msg)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(msg)
NameError: name 'msg' is not defined
>>> def counter():
	count = 0
	while True:
		count += 1
		return count

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	count = 0
	while True:
		count += 1
		yield count

		
>>> couter()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    couter()
NameError: name 'couter' is not defined
>>> counter()
<generator object counter at 0x0000016296FD3B88>
>>> adder = counter()
>>> next(adder)
1
>>> next(adder)
2
>>> next(adder)
3
>>> next(adder)
4
>>> counter()
<generator object counter at 0x0000016296FD3B88>
>>> next(adder)
5
>>> adder = counter()
>>> next(adder)
1
>>> def counter():
	count = 0
	while count < 5:
		count += 1
		yield count

		
>>> adder = counter()
>>> next(adder)
1
>>> next(adder)
2
>>> next(adder)
3
>>> next(adder)
4
>>> next(adder)
5
>>> next(adder)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    next(adder)
StopIteration
>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (i for i in range(10))
<generator object <genexpr> at 0x0000016296FD3B88>
>>> {x : x ** 3 for x in range(10)}
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> {i for i in range(10)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> def adder():
	    count = 0
	    def counter():
		c = count + 1
		yield c
	    return counter
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def adder():
	count = 0
	def counter():
		c = count + 1
		yield c
	return counter

>>> adder()
<function adder.<locals>.counter at 0x0000016296FF6BF8>
>>> c = adder()
>>> c()
<generator object adder.<locals>.counter at 0x0000016296FD3B88>
>>> x = c()
>>> next(x)
1
>>> next(x)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    next(x)
StopIteration
>>> def adder():
	count = 0
	def counter():
		c = count + 1
		return c
	yield counter

	
>>> adder()
<generator object adder at 0x0000016296FD3B88>
>>> x = adder()
>>> x
<generator object adder at 0x0000016297003A98>
>>> next(x)
<function adder.<locals>.counter at 0x0000016296FF6B70>
>>> next(x)()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    next(x)()
StopIteration
>>> x = adder()
>>> next(x)()
1
>>> 
