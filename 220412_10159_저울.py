n = int(input())
big = [set()for _ in range(n)]
small = [set()for _ in range(n)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    small[a-1].add(b-1)
    big[b-1].add(a-1)

for i in range(n):
    for s in small[i]:
        big[s].update(big[i])
    for b in big[i]:
        small[b].update(small[i])

#print(big)
#print(small)

for i in range(n):
    if len(big[i])+len(small[i]) < n-1:
        all = {i for i in range(n)}
        print(len(all.difference(big[i].union(small[i])))-1)
    else:
        print(0)