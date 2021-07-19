import random
import numpy as np
class Solution:
    def closestPairs(self, points):
        P = []
        for i in points:
            P.append(i)
        Px = self.mergeSort(P, 0)
        Py = self.mergeSort(P, 1)
        return self.DivideConquer(Px, Py)

    def DivideConquer(self, Px, Py):
        n = len(Px)

        if n == 1:
            return Px[0], (1000, 1000)
        if n == 2:
            return (Px[0], Px[1])
        best = Px[0], Px[1]
        Qx, Qy = Px[0:n//2], Py[0:n//2]
        Rx, Ry = Px[n//2:n], Py[n//2:n]
        p1, q1 = self.DivideConquer(Qx, Qy)
        p2, q2 = self.DivideConquer(Rx, Ry)
        d1, d2 = self.EuclideanDistance(p1, q1), self.EuclideanDistance(p2,q2)
        if d1 > d2:
            best = (p2, q2)
            delta = d2
        else:
            best = (p1, q1)
            delta = d1
        if len(Px) >= 2:
            p3, q3 = self.SplitPairs(Px, delta)
            d3 = self.EuclideanDistance(p3,q3)
            if delta >= d3:
                best = (p3, q3)
                delta = d3
        return best

    def SplitPairs(self, Px, delta):
        Sy = []
        n = len(Px)
        for point in Px:
            if abs(point[0] - Px[n//2][0]) < delta:
                Sy.append(point)
        Sy = self.mergeSort(Sy, 1)
        if len(Sy) < 2:
            return Px[0], Px[1]
        better = Sy[0], Sy[1]
        for i in range(len(Sy)):
            for j in range(i + 1, min(i + 8, len(Sy))):
                d = self.EuclideanDistance(Sy[i], Sy[j])
                if d < delta:
                    delta = d
                    better = (Sy[i], Sy[j])
        return better

    def mergeSort(self,nums, coordinate):
        n = len(nums)
        if n < 2:
            return nums
        a = self.mergeSort(nums[0:n // 2], coordinate)
        b = self.mergeSort(nums[n // 2:n], coordinate)
        c = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i][coordinate] <= b[j][coordinate]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        c += a[i::]
        c += b[j::]
        return c

    def EuclideanDistance(self, a, b):
        return np.sqrt(np.square(a[0] - b[0]) + np.square(a[1] - b[1]))

    def BruteForce(self, points):
        P = []
        for i in points:
            P.append(i)
        if len(P) < 2:
            return P
        distance = 1000
        best = P[0],P[1]
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                d = self.EuclideanDistance(P[i], P[j])
                if d < distance:
                    distance = d
                    best = P[i], P[j]
        return best
random.seed(48)
points = set((random.uniform(-5,5), random.uniform(-5,5)) for _ in range(1000))
import time
tic = time.time()
result = Solution().closestPairs(points)
toc = time.time()
print("分治用时" + str(toc - tic) + '秒')
brute = Solution().BruteForce(points)
tic = time.time()
print("暴力破解用时" + str(tic - toc) + '秒')