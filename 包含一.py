# __author__ = '31351'
def countone1(n):
    result = 0
    for i in range(1,n+1):
        for power in range(len(str(i)),-1,-1):
            if i/pow(10,power) == 1:
                result += 1
            i = i%pow(10,power)
    return result
#
# # print countone(20)
#
# output = []
# while True:
#     a = raw_input()
#     if a != '':
#         output.append(countone(int(a)))
#     else:
#         break
# for i in output:
#     print i

#-*- coding:utf-8 -*-
def countone2(x):
    result = 0
    for i in range(0, x+1):
        if '1' in str(i):
         # print 'True', i
         result += 1
    return result

def countone3(n):
    result = 0
    a = ''
    for i in range(n+1):
        a+=str(i)
    #print a
    for i in range(len(a)):
        if a[i] == '1':
            result+=1
    return result
def countone4(a,b):
    result = 0
    c = ''
    for i in range(a,b+1):
        c+=str(i)
    for i in range(len(c)):
        if c[i] == '1':
            result+=1
    return result

def countone5(n):
    k = n/1000
    result = 0
    a=0
    b=1
    if n < 1000:
        return countone3(n)
    else:
        while(a<k and b<k+1):
            result += countone4(a*1000+1,b*1000)
            a+=1
            b+=1
        result = result+countone4(k*1000+1,n)
    return result



if __name__ == '__main__':
    output = []
    while True:
        a = raw_input()
        if a != '':
            output.append(countone5(int(a)))
        else:
            break
    for i in output:
        print i
