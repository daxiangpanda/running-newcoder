__author__ = '31351'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prime(n):
    a = [0]*(n+1)
    primes = [0]*(n+1)
    len=0
    for i in range(2,n+1):
        if a[i] == 0:
            primes[len] = i
        len = len+1
        for j in range(2*i,n+1,i):
            a[j] = 1
    return primes

primes = prime(100000)
def primeadd(n):
    result = 0
    for i in primes:
        if n-i<2:
            break
        elif (n-i) in primes:
            result+=1
    return result/2

output = []
while True:
    a = raw_input()
    if a != '':
        output.append(primeadd(int(a)))
    else:
        break
for i in output:
    print i
