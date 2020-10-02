#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the organizingContainers function below.




def organizingContainers(arr):
    
    n=len(arr)
    csize=[0 for i in range(n)]
    tob=[0 for i in range(n)]
    for i in range(n):
        s=0
        for j in range(n):
            tob[j]+=arr[i][j]
            s+=arr[i][j]
        csize[i]+=s

    for i in range(n):
        flag=0
        m=tob[i]
        for j in range(n):
            if(m==csize[j]):
                flag = 1
                csize[j]=-1
                break
        if flag==0:
            return "Impossible"        

    return "Possible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
