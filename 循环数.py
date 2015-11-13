__author__ = '31351'

def func(a):
    b = a + a
    while True:
        for i in range(1,7):
            if str(int(a)*i) not in b:
                return False
            else:
                continue
        return True


# for i in range(100000000):
#     if func(str(i)):
#         print i
# a = '142857'
# print func(a)

if __name__ == '__main__':
    output = []
    while True:
        a = raw_input()
        if a != '':
            output.append(func(a))
        else:
            break
    for i in output:
        print i
