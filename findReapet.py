# -*- coding: utf-8 -*-
"""
    Created on Sun Sep  6 08:08:51 2015
    
    @author: WangS
"""


from __future__ import unicode_literals
import os

# This program is used to find repeat element in TXT.
# Check.txt is for original element and mayRepeat.txt is for element include repeat.
# Result.txt save the check results.

# PS:it may run twice.

os.chdir("/Users/genius/Desktop/LOOK/PulsarResult_WS")
f = open("findReapetResults.txt","w")

checkList=[]
mayRepeat = open('mayRepeat.txt', 'r')  # Put String in mayRepeat.txt, each String per line.

i = 0
for line in mayRepeat.readlines():
    i = i+1
    if line[-1] == '\n':  # If the last String is \n, delete.
        line = line[0:-1]
    
    if line in checkList:
        print("Repeat Element: %s at line%d (first line at LINE %d)\n" %(line, i, checkList.index(line)+1),file=f )
        # os and ,file=f can put print into Results.txt. Donot Forget \n! or you will get nothing :-)
        checkList[len(checkList):] = [''] # Give the space for the repeat element
    else:
        checkList[len(checkList):] = [line]


mayRepeat.close()



