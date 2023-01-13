# -*- coding: utf-8 -*-
"""

@author: Grivin
"""

"""Open text file and append words from each line to a list"""
f_in = open('wordsWM.csv','r')  # this files must be located in the same folder
                                # as the Jupyter notebook
data = f_in.readlines()
words = []
for line in data:
    words += line.split(',')
f_in.close()

"""Create a dictionary, create keys using the words in the passage, and count
   the number of occurrences of each word, using that quantity as a value """
wordDict = {}
bins = list(set(words))
for b in bins:
    wordDict[b] = 0
for word in words:
    #if word not in stopWords:
    wordDict[word] += 1

""" Create spearate lists for the x variables (keys) and y variables (values)"""
xVar = []
yVar = []
for k,v in wordDict.items():
    xVar.append(k)
    yVar.append(v)

"""Write the dictionary data into a text file"""
f_out = open('wordsWMDict.csv','w')
for k,v in wordDict.items():
    f_out.write(str(k) + ',' + str(v) + '\n')
f_out.close()