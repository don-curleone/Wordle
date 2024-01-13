#!/usr/bin/python3

# yellow = * 
# green = same letter

import sys
import random

with open("./5_letter_words.txt", 'r', encoding='utf-8', newline='') as allwords:
    allwords = list(allwords)
    ans = random.choice(allwords)
    ans = ans.lower()

used = []
hints = ["_", "_", "_", "_", "_"]

def play():
    global word
    word = str(input()).lower()

    if len(word) != 5 :
        sys.exit("\nenter a 5 lettered word")
    
    word = list(word)

    # logic
    for x in range(len(word)):
        if(word[x] == ans[x]):
            hints[x] = word[x]
            used.append(word[x])
        elif(word[x] in ans and word[x] not in used):
            hints[x] = "*"

    print(*word)
    print(*hints)
    print("")


for i in range(6):
    play()
    if("_" not in hints):
        sys.exit("You won!")
    hints = ["_", "_", "_", "_", "_"]

print("correct word is " + ans)