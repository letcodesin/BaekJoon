alist = []
plist = []
num = int(input())
a = input()

a = a.split(' ')

for i in range(0, num):
    alist.append([int(a[i]), i])
    plist.append(0)


alist.sort()

for i in range(0, num):
    plist[alist[i][1]] = i

for i in range(0, num):
    print(plist[i], end=" ")