# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def attire(temp):
    if temp <= 32:
        choice = 'Wear wool overcoat'
    elif temp < 80:
        choice = 'Wear sport coat or suit'
    else:
        choice = 'Loosen Tie'

    return choice

temperature = 99
clothes = attire(temperature)
print(clothes)