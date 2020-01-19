Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py", line 5, in <module>
    print("Sum is"+c)
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
>>> name = "Ram"
>>> sal = 23000
>>> msg = "Hello " + name + " your salary is " + sal
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    msg = "Hello " + name + " your salary is " + sal
TypeError: can only concatenate str (not "int") to str
>>> msg = "Hello ", name , " your salary is ", sal
>>> msg
('Hello ', 'Ram', ' your salary is ', 23000)
>>> msg = "Hello {}, your name is {}".format(name,sal)
>>> msg
'Hello Ram, your name is 23000'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonWE_Morning/Codes/01_Print.py 
34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
Sum is 34
Sum of 12 and 22 is 34
Sum of 12 and 22 is 34
>>> id(12)
140704246490096
>>> id
<built-in function id>
*
>>> id(10)
140704246490032
>>> a = 10
>>> id(a)
140704246490032
>>> a = 2038094928492384798234798237498237498
>>> type(int)
<class 'type'>
>>> type(a)
<class 'int'>
>>> import sys
>>> a = 10
>>> sys.getsizeof(a)
28
>>> a = 1000
>>> sys.getsizeof(a)
28
>>> a = 1000000
>>> sys.getsizeof(a)
28
>>> a = 100000000
>>> sys.getsizeof(a)
28
>>> a = 10000000000
>>> sys.getsizeof(a)
32
>>> a = 0
>>> sys.getsizeof(a)
24
>>> sys.getsizeof(int)
400
>>> sys.getsizeof(int())
24
>>> isinstance(a,int)
True
>>> msg = "hello ramesh, how are you ?"
>>> msg.encode()
b'hello ramesh, how are you ?'
>>> bytes(msg)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    bytes(msg)
TypeError: string argument without an encoding
>>> bytes(msg, encoding='utf-8')
b'hello ramesh, how are you ?'
>>> recv = b'hello ramesh, how are you ?'
>>> recv.decode()
'hello ramesh, how are you ?'
>>> msg = "हैलो रमेश, आप कैसे हैं?"
>>> msg.encode()
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\xb0\xe0\xa4\xae\xe0\xa5\x87\xe0\xa4\xb6, \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> msg = "हैलो रमेश, आप कैसे हैं, long time no see"
>>> msg.encode()
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\xb0\xe0\xa4\xae\xe0\xa5\x87\xe0\xa4\xb6, \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82, long time no see'
>>> recv = msg.encode()
>>> recv.decode()
'हैलो रमेश, आप कैसे हैं, long time no see'
>>> 
