Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "hello John"
>>> print(a)
hello John
>>> a = 'hello "John"'
>>> print(a)
hello "John"
>>> a = """'hello "John"'"""
>>> print(a)
'hello "John"'
>>> path = "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2019\December\Python_Reg_3\PythonNewEnv"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = r"C:\User\asus\Documents\Data\DataTransfer\BMPL_Batches\2019\December\Python_Reg_3\PythonNewEnv"
>>> msg = "hello, how are you ?"
>>> bytes(msg)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    bytes(msg)
TypeError: string argument without an encoding
>>> bytes(msg,encoding='utf-8')
b'hello, how are you ?'
>>> msg = "हैलो जॉन, आप कैसे हैं?"
>>> bytes(msg,encoding='utf-8')
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x9c\xe0\xa5\x89\xe0\xa4\xa8, \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> encoded_msg = bytes(msg,encoding='utf-8')
>>> encoded_msg
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x9c\xe0\xa5\x89\xe0\xa4\xa8, \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> encoded_msg.decode()
'हैलो जॉन, आप कैसे हैं?'
>>> encoded_msg[0]
224
>>> encoded_msg[1]
164
>>> encoded_msg[2]
185
>>> for x in encoded_msg:
	print(x)

	
224
164
185
224
165
136
224
164
178
224
165
139
32
224
164
156
224
165
137
224
164
168
44
32
224
164
134
224
164
170
32
224
164
149
224
165
136
224
164
184
224
165
135
32
224
164
185
224
165
136
224
164
130
63
>>> msg = "hello, how are you ?"
>>> encoded_msg = bytes(msg)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    encoded_msg = bytes(msg)
TypeError: string argument without an encoding
>>> encoded_msg = bytes(msg,encoding='utf-8')
>>> encoded_msg
b'hello, how are you ?'
>>> encoded_msg[0]
104
>>> encoded_msg[1]
101
>>> for x in encoded_msg:
	print(x)

	
104
101
108
108
111
44
32
104
111
119
32
97
114
101
32
121
111
117
32
63
>>> for x,y in zip(msg,encoded_msg):
	print(x,"===>",y)

	
h ===> 104
e ===> 101
l ===> 108
l ===> 108
o ===> 111
, ===> 44
  ===> 32
h ===> 104
o ===> 111
w ===> 119
  ===> 32
a ===> 97
r ===> 114
e ===> 101
  ===> 32
y ===> 121
o ===> 111
u ===> 117
  ===> 32
? ===> 63
>>> 
