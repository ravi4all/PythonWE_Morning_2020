# def emp(id,name,*dept,address=None):
#     print("Emp details")
#     print("Id is",id)
#     print("Name is",name)
#     print("Dept is",dept)
#     print("Address is",address)
#
# emp(101,'Ram','HR','IT',address='Rohini')
# emp(102,'Ramesh','IT','Pune','Delhi')
# emp(103,'Aman','IT','Pune','Delhi','Noida')

# kwargs - keyword arguments
def emp(**details):
    print(details)

emp(name='Ram',dept='IT')
emp(name='Raman',address='Delhi',dept='IT')
emp(id=104,dept='HR',sal=45000)