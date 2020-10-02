import math

def gcd( a,  b):
    #print(a,":",b)
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

def count(n):
    
    c=0
    m=int(math.sqrt(n))
    for i in range(1,m+1):
            
        if n%i==0:
            c+=2
            if n/i==i:
                c-=1
    return c
    
a,b=map(int,input().split(' '))

print(count(gcd(a,b)))