__author__ = '31351'
import sys
sys.setrecursionlimit(1000000000)
def f(n):
    if n==0:
        return ''
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        i=2
        while True:
            if n%i==0:
                return f(n-1)
            i=i+1
            if i>=n:
                return f(n-1)+1
output = []
while True:
    a = raw_input()
    if a != '':
        if a!= 0:
            output.append(f(int(a)))
        else:
            output.append('\n')
    else:
        break
for i in output:
    print i
