# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:09:03 2025

@author: Bregi
"""

import os

path = "C:/Users/Bregi/Documents/GitHub/dabibble/bible"
dir_list = os.listdir(path)
bibble = list()
better_bibble = list()
bible_prompt = 0
in_the_bible = list()

for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            # parse inner data
            with open(path + "/" + f, 'r', encoding="utf8") as a:
                for item in (a.read().split(' ')):
                    bibble.append(item.lower())

# clear newline characters
for i in bibble:
    i = ''.join([char for char in i if char.isalpha()])
    better_bibble.append(i)
    
bibble_dupeless = list(dict.fromkeys(better_bibble))

print ("please prompt with your dumbass post:")

# User provided information
user_prompt = input()
user_prompt = user_prompt.split(' ')

for entry in user_prompt:
    if entry in bibble_dupeless:
        bible_prompt += 1
        in_the_bible.append(entry)

percent_in_bible = round(bible_prompt / len(user_prompt), 2) * 100
print("Your post is " + str(percent_in_bible) + "% in the bible")
print("your entries from the bible were:")
print(in_the_bible)