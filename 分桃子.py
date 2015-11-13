__author__ = '31351'

def peach(n):
    a = pow(5,n)
    b = pow(4,n)
    return a-4,b-4+n

output = []
while True:
    a = raw_input()
    if a != '':
        if int(a)!= 0:
            output.append(peach(int(a)))
        else:
            output.append('\n')
    else:
        break
for i in output:
    print list(i)
