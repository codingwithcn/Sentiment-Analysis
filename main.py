# Code by Chidozie J. Nnaji
# Licensed under Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
from model import *

wrong = 0
right = 0
length = 0
# You can use this to check what the AI got wrong or right by saving it to the dictionary.
wrongs = {}
rights = {}
# This for loop test the AI accuracy
for test in emotions_test.items():
    dic = test[1]
    if type(dic) == list:
        for word in dic:
            length += 1
            see = preprocess(word)
            if see[0]:
                yes = False
                close = False
                for check in see[2]:
                    emo = check[1]
                    if test[0] in emo:
                        yes = True
                    else:
                        for last in see[3]:
                            emo = last[1]
                        if test[0] in emo:
                            close = True
                if yes == True:
                    right += 1
                elif close == True:
                    right += 0.5
                else:
                    wrong += 1
            else:
                wrong += 1
    else:
        length += 1
        see = preprocess(dic)
        if see[0]:
            yes = False
            close = False
            for check in see[2]:
                emo = check[1]
                if test[0] in emo:
                    yes = True
                else:
                    for last in see[3]:
                        emo = last[1]
                    if test[0] in emo:
                        close = False
            if yes == True:
                right += 1
            elif close == True:
                right += 0.5
            else:
                wrong += 1
        else:
            wrong += 1
print("Your AI emotion detection is " + str((right / length) * 100) + ' accurate')
print(right, wrong, length)
