import itertools
count = int(input())
num = list(map(int, input().split()))
ycount = list(map(int, input().split()))
yonsan = []
for i in range(4):
    if i == 0:
        for _ in range(ycount[i]):
            yonsan.append('+')
    elif i == 1:
        for _ in range(ycount[i]):
            yonsan.append('-')
    elif i == 2:
        for _ in range(ycount[i]):
            yonsan.append('*')
    elif i == 3:
        for _ in range(ycount[i]):
            yonsan.append('//')
#print(yonsan)
ylist = list(itertools.permutations(yonsan))
#print(ylist)

min = 1e10
max = -1e10

#result = []
for i in range(len(ylist)):
    temp = num[0]
    for j in range(len(ylist[i])):
        if ylist[i][j] == '+':
            temp += num[j+1]
        elif ylist[i][j] == '-':
            temp -= num[j+1]
        elif ylist[i][j] == '*':
            temp *= num[j+1]
        elif ylist[i][j] == '//':
            if temp < 0:
                temp = -(-temp // num[j+1])
            else:
                temp = temp // num[j+1]
    #result.append(temp)
    if temp < min:
        min = temp
    if temp > max:
        max = temp
#print(result)
print(max)
print(min)


########################upgrade solution############################
count = int(input())
num = list(map(int, input().split()))
add, sub, mult, div = map(int, input().split())

minnum = 1e10
maxnum = -1e10

def dfs(i, temp):
    global add, sub, mult, div, minnum, maxnum
    if i == count:
        minnum = min(minnum, temp)
        maxnum = max(maxnum, temp)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, temp + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, temp - num[i])
            sub += 1
        if mult > 0:
            mult -= 1
            dfs(i+1, temp * num[i])
            mult += 1
        if div > 0:
            div -= 1
            if temp < 0:
                dfs(i+1, -(-temp // num[i]))
            else:
                dfs(i+1, temp // num[i])
            div += 1

dfs(1, num[0])
print(maxnum)
print(minnum)

#참고: https://data-flower.tistory.com/72