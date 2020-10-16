#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mixColors' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY colors
#  2. 2D_INTEGER_ARRAY queries
#


r_dict={}
b_dict={}
g_dict={}
def createdict(t):
    if(t[0] in r_dict):
        if(t[1] in r_dict[t[0]]):
            if(not(t[2] in r_dict[t[0]][t[1]])):
                r_dict[t[0]][t[1]].append(t[2])
        else:
            r_dict[t[0]][t[1]]=[]
            r_dict[t[0]][t[1]].append(t[2])
    else:
        r_dict[t[0]]={}
        r_dict[t[0]][t[1]]=[]
        r_dict[t[0]][t[1]].append(t[2])
    if(t[1] in b_dict):
        if(t[0] in b_dict[t[1]]):
            if(not(t[2] in b_dict[t[1]][t[0]])):
                b_dict[t[1]][t[0]].append(t[2])
        else:
                b_dict[t[1]][t[0]]=[]
                b_dict[t[1]][t[0]].append(t[2])
    else:
        b_dict[t[1]]={}
        b_dict[t[1]][t[0]]=[]
        b_dict[t[1]][t[0]].append(t[2])
    if(t[2] in g_dict):
        if(t[0] in g_dict[t[2]]):
            if(not(t[1] in g_dict[t[2]][t[0]])):
                g_dict[t[2]][t[0]].append(t[1])
        else:
                g_dict[t[2]][t[0]]=[]
                g_dict[t[2]][t[0]].append(t[1])
    else:
        g_dict[t[2]]={}
        g_dict[t[2]][t[0]]=[]
        g_dict[t[2]][t[0]].append(t[1])

def check_perform(t):
    check_counter={'r':False,'b':False,'g':False}
    if(t[0] in r_dict and t[1] in b_dict and t[2] in g_dict):
        for i in r_dict[t[0]]:
            if(i<=t[1]):
                for j in r_dict[t[0]][i]:
                    if(j<=t[2]):
                        check_counter['r']=True
                        break
            if(check_counter['r']is True):
                break

        for i in b_dict[t[1]]:
            if(i<=t[0]):
                for j in b_dict[t[1]][i]:
                    if(j<=t[2]):
                        check_counter['b']=True
                        break
            if(check_counter['b']is True):
                break

        for i in g_dict[t[2]]:
            if(i<=t[0]):
                for j in g_dict[t[2]][i]:
                    if(j<=t[1]):
                        check_counter['g']=True
            if(check_counter['g']is True):
                break

    if(check_counter['r']is True and check_counter['b']is True and check_counter['g']is True):
        return("YES")
    else:
        return("NO")

def mixColors(colors, queries):
    # Write your code here
    s=[]
    nd=len(colors)
    nq=len(queries)
    for i in range(nd):
        t=colors.pop()
        createdict(t)
    print(r_dict)
    print(b_dict)
    print(g_dict)

    for i in range(nq):
        t=queries[i]
        s.append(check_perform(t))
    return(s)
x =[[1, 3, 5], [5, 3, 1], [1,2,2],[1,1,1],[3,4,4]]

y =[[5, 3, 5], [3, 3, 3]]

print(x)
print(mixColors(x,y))
