def bfs():
    queue = []
    queue.append(soobin)
    while queue:
        at = queue.pop(0)
        if at == sister:
            print(visited_dist[at])
            route = []
            node = sister
            #route.append(node)
            #while prenode[node] != soobin: # 시간초과 
            for i in range(visited_dist[sister] + 1):
                route.append(node)
                node = prenode[node]
            #route.append(soobin)
            print(' '.join(map(str, route[::-1])))
            return visited_dist[at]
        for goto in [at + 1, at - 1, at * 2]:
            if 0 <= goto <= 1000000 and visited_dist[goto] == 0:
                queue.append(goto)
                visited_dist[goto] = visited_dist[at] + 1
                prenode[goto] = at
    
soobin, sister = map(int, input().split(' '))
visited_dist = [0 for _ in range(1000001)]
prenode = [0 for _ in range(1000001)]
bfs()


