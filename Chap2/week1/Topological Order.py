class TOrder:
    def DFS_Loop(self,Graph):
        n = len(Graph)
        visited = [False for i in range(n + 1)]
        f_s = [n for i in range(n)]
        cur_label = n

        def DFS(G, s):
            nonlocal cur_label
            nonlocal f_s
            for v in G[s]:
                if not visited[v]:
                    DFS(G,v)
            visited[s] = True
            f_s[s - 1] = cur_label
            cur_label -= 1

        for vertex in Graph:
            if visited[vertex] == False:
                DFS(Graph, vertex)
        return f_s



file = open('TOrder.txt','r')
Graph = dict()
for line in file:
    cur = line.split()
    cur = map(int, cur)
    cur = list(cur)
    Graph[cur[0]] = set()
    for i in range(1, len(cur)):
        Graph[cur[0]].add(cur[i])

print(TOrder().DFS_Loop(Graph))