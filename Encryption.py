#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):

    n=len(s)
    r=int(math.ceil(math.sqrt(n)))
    c=int(math.floor(math.sqrt(n)))
    if (r*c)<n:
        c+=1
    k=""
    for i in range(r):
        for j in range(c):
            if((i+j*r)<n):
                k+=s[i+r*j]
        k+=" "
    return k



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
