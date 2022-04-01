n = int(input())
sik = list(input())
gap = [float(input())for _ in range(n)]
#print(sik)
#print(gap)
for i in range(len(sik)):
    if sik[i] != '+' and sik[i] != '-' and sik[i] != '*' and sik[i] != '/':
        gidx = ord(sik[i])-ord('A')
        sik[i] = gap[gidx]
#print(sik)

i=0
while i < len(sik):
    if sik[i] == '+' or sik[i] == '-' or sik[i] == '*' or sik[i] == '/':
        b = sik[i-1]
        a = sik[i-2]
        #print(sik[i], a, b)
        if sik[i] == '+':
            sik.insert(i+1, a+b)
            #print(sik)
            sik.pop(i)
            sik.pop(i-1)
            sik.pop(i-2)
            #print(sik)
            i = 0    
        elif sik[i] == '-':
            sik.insert(i+1, a-b)
            #print(sik)
            sik.pop(i)
            sik.pop(i-1)
            sik.pop(i-2)
            #print(sik)
            i = 0    
        elif sik[i] == '*':
            sik.insert(i+1, a*b)
            #print(sik)
            sik.pop(i)
            sik.pop(i-1)
            sik.pop(i-2)
            #print(sik)
            i = 0
        elif sik[i] == '/':
            sik.insert(i+1, a/b)
            #print(sik)
            sik.pop(i)
            sik.pop(i-1)
            sik.pop(i-2)
            #print(sik)
            i = 0
    else:
        i += 1

print("{:.2f}".format(sik[0]))

#############################upgrade solution#############################
n = int(input())
sik = list(input())
gap = [float(input())for _ in range(n)]

stack = []
for i in range(len(sik)):
    if 'A' <= sik[i] <= 'Z':
        stack.append(gap[ord(sik[i])-ord('A')])
    else: #연산자일때
        b = stack.pop()
        a = stack.pop()
        if sik[i] == '+':
            stack.append(a + b)
        elif sik[i] == '-':
            stack.append(a - b)
        if sik[i] == '*':
            stack.append(a * b)
        if sik[i] == '/':
            stack.append(a / b)
print("{:.2f}".format(stack[0]))
        