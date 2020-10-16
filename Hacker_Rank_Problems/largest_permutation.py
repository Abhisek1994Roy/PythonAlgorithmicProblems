#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def swapPositions(num_list, pos1, pos2):
    num_list[pos1], num_list[pos2] = num_list[pos2],num_list[pos1]
    return num_list

def largestPermutation(k, arr):
    pos1=0
    arr_copy = list(arr)
    if k>(len(arr)):
        return list(reversed(list(sorted(arr))))
    for i in range(0, k):
        j = max(arr_copy)
        print("-----------------------")
        print(j)
        pos2=arr.index(j)
        arr = swapPositions(arr, pos1, pos2)
        pos1+=1
        arr_copy[arr_copy.index(j)]=-1111111
        print(arr_copy)
    return arr

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)
    print(result)
