#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.

def minafter(arr,l):
   
    i2=l+1
    for i in range(l,len(arr)):
        if arr[i]>arr[l] and arr[i]<arr[i2]:
            i2=i
    
    return i2        


def biggerIsGreater(w):

    w=list(w)
    flag=0
    i1=0
    i2=0    
    for i in range(len(w)-1,0,-1):
        if w[i]>w[i-1]:
            i1=i-1
            i2=minafter(w,i-1)
            flag=1
            break
    if flag==0:
        return "no answer"
                
    temp=w[i1]
    w[i1]=w[i2]
    w[i2]=temp
    w=w[:i1+1]+sorted(w[i1+1:])
    """arr=list(map(chr,arr))"""
    arr=''.join(w)
    return arr    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
