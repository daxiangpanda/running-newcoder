def comp(a,b):
    if a>b:
        return 'Yes'
    else:
        return 'No'
output = []
while True:
    a = raw_input().split(' ')
    n = a[0]
    r = a[1]
    c = 2*3.14*int(r)
    if a != '':
        output.append(comp(int(n),int(c)))
    else:
        break
for i in output:
    print i
#
# a = raw_input().split()
# print a