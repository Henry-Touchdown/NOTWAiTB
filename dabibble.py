# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:09:03 2025

@author: Bregi
"""

import os

path = "C:/Users/Bregi/Documents/GitHub/dabibble/bible"
dir_list = os.listdir(path)

for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            # parse inner data
            with open(path + "/" + f, 'r', encoding="utf8") as a:
                print(a.read())