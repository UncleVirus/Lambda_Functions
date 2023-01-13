# -*- coding: utf-8 -*-
"""

@author: Grivin
"""

f = lambda x:x**2
y = f(2)
print(y)

g = lambda x:x[0]
z = g([0,1,2])
print(z)

h = lambda x,y:max(x,y)**2
x = h(2,3)
print(x)

j = lambda x: 'even' if x%2 == 0 else 'odd'
x = 5
print(x,' is ',j(x))
x = 6

print(x,' is ',j(x))
''' lambda function, which is assigned to the variable x,
that accepts a Boolean value (True or False) and returns an integer 1 
if True is passed to the lambda function 
and 0 if False is passed to the lambda function.
 Assuming only True or False values are passed as argument '''
x = lambda val: 1 if val else 0
#testing if it is true 
print(x(True))
#Testing if it is false
print(x(False))

''' lambda function using the variable y that receives
a list and returns the type of the first data element (with index 0) 
in that list. Assuming list is not empty '''

y = lambda aList: type(aList[0])

#testing <class 'str'>
print(y(["hello", 1, 2, 3]))

#testing <class 'int'>
print(y([1, 2, 3]))


''' lambda function using the variable z that implements 
the factorial function. the function returns 1 if n is 0 or 1
 otherwise multiplies n with value returned by z(n-1) and return it. 
 Assuming n>=0 '''
 
z = lambda n: 1 if n <= 1 else n * z(n - 1)

#testing 6
print(z(3))
#testing 120
print(z(5))
# testing 362880
print(z(9))