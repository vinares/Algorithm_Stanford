import time
import heapq
class dijkstra:

    def adjacentList(self, file):
        f = open(file, 'r')
        adjacent = []
        for line in f:
            adjacent.append([])
            data = line.split()
            v = int(data[0]) - 1
            for i in range(1, len(data)):
                cur = data[i].split(',')
                w = int(cur[0]) - 1
                edge_length = int(cur[1])
                adjacent[v].append((w,edge_length))

        return adjacent

    def array_based_dijkstra(self, adjacent_list, source):
        n = len(adjacent_list)
        pq = [i for i in range(n)]
        pq[0], pq[source] = pq[source], pq[0]
        infinity = 1000000
        A = [infinity] * n
        A[source] = 0
        #B = [[]] * n
        visited = [False] * n

        while pq:
            v = self.arrayBased(pq, A)
            visited[v] = True

            for w, edge in adjacent_list[v]:
                if not visited[w]:
                    new_edge = A[v] + edge
                    if A[w] > new_edge:
                        A[w] = new_edge
                        #B[w] = B[v] + [(v,w)]

        return A

    def heap_Based_dijkstra(self, adjacent_list, source):
        n = len(adjacent_list)
        infinity = 1000000

        A = [infinity] * n
        A[source] = 0
        #B = [[]] * n

        pq = [(A[i], i) for i in range(n)]
        heapq.heapify(pq)

        visited = [False] * n
        while pq:
            v = heapq.heappop(pq)[1]
            if visited[v]:continue
            visited[v] = True
            for w, edge in adjacent_list[v]:
                if not visited[w]:
                    new_edge = A[v] + edge
                    if A[w] > new_edge:
                        A[w] = new_edge
                        #B[w] = B[v] + [(v, w)]
                        heapq.heappush(pq, (A[w],w))
        return A


    def arrayBased(self, pq, A):
        min_distance = A[pq[0]]
        i = 0
        j = 1
        while j < len(pq):
            if A[pq[j]] < min_distance:
                min_distance = A[pq[j]]
                i = j
            j += 1
        res = pq[i]
        pq[i] = pq[-1]
        pq.pop()

        return res

    def main(self, file='dijkstraData.txt',source=1, end=None):
        adjacent_list = self.adjacentList(file)
        res = []

        tic = time.time()
        A = self.array_based_dijkstra(adjacent_list, source - 1)
        toc = time.time()
        print("O(n^2),array based dijkstra algorithm takes: "+str("%.6f"%(toc - tic))+"s")

        tic = time.time()
        A = self.heap_Based_dijkstra(adjacent_list, source - 1)
        toc = time.time()
        print("O(n * log(n),heap based dijkstra algorithm takes: "+str("%.6f"%(toc - tic))+"s")

        for i in range(len(end)):
            res.append(A[end[i] - 1])

        return ','.join(map(str,res))


source = 1
end = [7,37,59,82,99,115,133,165,188,197]
print(dijkstra().main(file='dijkstraData.txt',source=source, end=end))