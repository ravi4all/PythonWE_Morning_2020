Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {'name':'Aman','college':'IP','marks':78,'address':"Rohini"}
>>> d
{'name': 'Aman', 'college': 'IP', 'marks': 78, 'address': 'Rohini'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Aman'
>>> d['hobby'] = 'football'
>>> d
{'name': 'Aman', 'college': 'IP', 'marks': 78, 'address': 'Rohini', 'hobby': 'football'}
>>> d.keys()
dict_keys(['name', 'college', 'marks', 'address', 'hobby'])
>>> d.values()
dict_values(['Aman', 'IP', 78, 'Rohini', 'football'])
>>> d.items()
dict_items([('name', 'Aman'), ('college', 'IP'), ('marks', 78), ('address', 'Rohini'), ('hobby', 'football')])
>>> for item in d:
	print(item)

	
name
college
marks
address
hobby
>>> for item in d:
	print(d[item])

	
Aman
IP
78
Rohini
football
>>> for item in d:
	print(item,":",d[item])

	
name : Aman
college : IP
marks : 78
address : Rohini
hobby : football
>>> d.get('name')
'Aman'
>>> d['name']
'Aman'
>>> d['names']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d['names']
KeyError: 'names'
>>> d.get('names')
>>> 
