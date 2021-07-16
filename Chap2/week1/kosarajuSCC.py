from collections import defaultdict
import numpy as np
import sys
import threading
import time
class Kosaraju:
    def __init__(self):
        self.t = 0
        self.n = 0
        self.s = None
        self.visited = []
        self.finishing_times = []
        self.leader = []


    def DFS_Loop(self, G, order):
        self.t = 0
        self.s = None
        self.visited = [False for _ in range(self.n)]
        self.finishing_times = [self.n for _ in range(self.n)]
        self.leader = [0 for _ in range(self.n)]
        for i in order:
            if not self.visited[i]:
                self.s = i
                self.DFS(G,i)
        return

    def DFS(self,G,i):
        self.visited[i] = True
        self.leader[self.s] += 1
        if G[i + 1]:
            for x in G[i + 1]:
                if len(self.visited) <= x - 1:
                    print(x, len(self.visited))
                if not self.visited[x - 1]:
                    self.DFS(G,x - 1)
        self.t += 1
        self.finishing_times[i] = self.t
        return



    def kosaraju(self, G, G_rev):

        self.n = max(len(G),len(G_rev))
        order = [i for i in range(len(G_rev))]
        self.DFS_Loop(G_rev, order)
        finishing_times = [0 for i in range(self.n)]
        for i, val in enumerate(self.finishing_times):
            finishing_times[self.n - val] = i
        order = finishing_times
        self.DFS_Loop(G, order)
        return self.leader


def main():
    tic = time.time()

    file = open('SCC.txt', 'r')
    Graph = []
    Graph_rev = []

    for line in file:
        cur = line.split()
        cur = list(cur)
        head, tail = int(cur[0]) - 1, int(cur[1]) - 1
        max_vertex = max(head,tail) + 1

        while len(Graph) < max_vertex:
            Graph.append([])
        while len(Graph_rev) < max_vertex:
            Graph_rev.append([])

        Graph[head].append(tail)
        Graph_rev[tail].append(head)
    ans = Kosaraju().kosaraju(Graph, Graph_rev)

    res = ','.join(map(lambda x:str(x),sorted(ans)[::-1][:5]))
    print(res)
    print(time.time() - tic)
    return

if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target