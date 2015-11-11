__author__ = '31351'

from math import sqrt
N = 100000
prime = [p for p in range(2, N) if 0 not in [p % d for d in range(2, int(sqrt(p))+1)]]
sum = [i+j for i in prime for j in prime]
num = 0
for i in range(100000):
    if i in sum:
        num+=1
print num
print len(sum)
