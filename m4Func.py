# -*- coding: utf-8 -*-
"""

@author: Grivin
"""

#function to print sum
def sumEven(myDict):
    
    sum=0
    for i in myDict:
        if  myDict[i]%2 == 0:
            sum = sum + myDict[i]
    return sum


#Driver function
dict = {'a' : 100, 'b':200, 'c':300}
print("Sum :", sumEven(dict))
    