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
N=10000
primes = prime(N)
# print primes
print len(primes)
count = [0]*(N*2)
# print count
print len(count)
print count
for i in range(0,N):
    for j in range(i+1,N):
        if primes[i] == 0 or primes[j] == 0:
            continue
        elif primes[i]+primes[j] > N:
            break
        else:
            count[primes[i]+primes[j]]+=1
print count
output = []
while True:
    a = raw_input()
    if a != '':
        output.append(count[int(a)])
    else:
        break
for i in output:
    print i
