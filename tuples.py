# -*- coding: utf-8 -*-
"""
@author: Grivin
"""

""" Lists are defined with square brackets """
""" Example list structures """
list1 = [0,1]               # List of integers           
list2 = ['a','b']           # List of strings            
list3 = [0,'b']             # List of mixed data types   
list4 = [0,1,'a','b']       # Lists of arbitrary lengths 
list5 = [[0,1],[2,3]]       # Lists of lists   
list6 = [[[0,1],[2,3]],
         [[0,1],[2,3]]]     # Lists of lists of lsit
list7 = [[0,['NYC',10000]], 
         [1,['CHI',7500]]]  # Custom formatted lists 

for i in range(len(list1)):
    print(list1[i])         # Retrieve list elements
list1[1] = 9                # Change a list element
print(list1[1])             # View the change

""" Tuples are defined with parentheses """
tup1 = (0,1)                # Tuple of integers           
tup2 = ('a','b')            # Tuple of strings            
tup3 = (0,'b')              # Tuple of mixed data types   
tup4 = (0,1,'a','b')        # Tuple of arbitrary lengths
tup5 = ((0,1),(2,3))        # Tuple of lists             
tup6 = ((0,('NYC',10000)), 
        (1,('CHI',7500)))   # Custom formatted tuple 

mix1 = [(0,('NYC',10000)), 
        (1,('CHI',7500))]   # List of tuples

for i in range(len(list1)):
    print(tup1[i])          # Retrieve tuple elements
tup1[1] = 9                 # Try to change a list element