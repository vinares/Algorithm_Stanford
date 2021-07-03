import numpy as np
import copy
import time
count = 0


def contraction(Graph):
    n = len(Graph)
    vertices = list(Graph.keys())
    if n == 2:
        return Graph[vertices[0]][vertices[1]], (vertices[0], vertices[1])
    vertex_a = np.random.choice(vertices)
    edges_a = list(Graph[vertex_a].keys())
    vertex_b = np.random.choice(edges_a)
    edges_b = list(Graph[vertex_b].keys())

    for contact in edges_b:
        if contact != vertex_a:
            if contact not in Graph[vertex_a]:
                Graph[vertex_a][contact] = Graph[vertex_b][contact]
            else:
                Graph[vertex_a][contact] += Graph[vertex_b][contact]
            if vertex_a not in Graph[contact]:
                Graph[contact][vertex_a] = Graph[vertex_b][vertex_a]
            else:
                Graph[contact][vertex_a] += Graph[vertex_b][vertex_a]
            del Graph[contact][vertex_b]


    del Graph[vertex_a][vertex_b]
    if vertex_a in Graph[vertex_a]:
        del Graph[vertex_a][vertex_a]
    del Graph[vertex_b]
    return contraction(Graph)

def minCut(graph):
    global count

    n = len(graph.keys())
    N = int(n ** 2 * np.log(n))
    crossing_edges = len(graph[1])
    minimum_cuts = set()

    for _ in range(N):
        copygraph = copy.deepcopy(graph)
        count += 1
        if count % 1000 == 0:
            print(count)
        cur_cross, cur_cuts = contraction(copygraph)
        if cur_cross < crossing_edges:
            crossing_edges = cur_cross
            minimum_cuts = set()
            minimum_cuts.add(cur_cuts)
        elif cur_cross == crossing_edges:
            minimum_cuts.add(cur_cuts)
    return crossing_edges, minimum_cuts

print(count)



file = open('kargerMinCut.txt','r',)
graph = dict()

for line in file:
    cur = line.split()
    cur = map(int,cur)
    cur = list(cur)
    graph[cur[0]] = dict()
    for i in range(1,len(cur)):
        graph[cur[0]][cur[i]] = 1

tic = time.time()
print(minCut(graph))
toc = time.time() - tic
print('O(n^2 logn) trials took: '+str(toc) +' seconds.')