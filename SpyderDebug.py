# -*- coding: utf-8 -*-
"""

@author: Grivin
"""

def attire(temp):
    if temp <= 32:
        choice = 'Wear wool overcoat'
    elif temp < 80:
        choice = 'Wear sport coat or suit'
    else:
        choice = 'Loosen Tie'


temperature = 99
clothes = attire(temperature)
print(clothes)