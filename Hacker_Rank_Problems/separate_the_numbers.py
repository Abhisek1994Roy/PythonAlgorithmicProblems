# Solution to the problem - https://www.hackerrank.com/challenges/separate-the-numbers/problem
# Separate the Numbers


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    flag = True
    val_arr = []
    first_val_arr = []

    if len(s)==1:
        print("NO")
    else:
        for i in range(1, (len(s)//2)+1):
            first_val=s[:i]
            # print(first_val)
            new_val=""
            first_val_arr.append(first_val)
            while(len(new_val+first_val)<=len(s)):
                new_val = new_val+first_val
                first_val = str(int(first_val)+1)
            val_arr.append(new_val)
        # print(val_arr)
        if s in val_arr:
            print("YES",first_val_arr[(val_arr.index(s))])
        else:
            print("NO")


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
