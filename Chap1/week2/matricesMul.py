import numpy as np
import time
class Solutions:
    def bruteForce(self,X, Y):
        n = len(X)
        ans = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                ans[i][j] = 0
                for k in range(n):
                    ans[i][j] += (X[i][k] * Y[k][j])
        return ans

    def divideAndConquer(self, X, Y):
        n = len(X)
        if n < 2:
            ans = np.zeros((1,1))
            ans[0][0] = X[0][0] * Y[0][0]
            return ans

        A, E = X[0:n//2,0:n//2], Y[0:n//2,0:n//2]
        B, F = X[0:n//2,n//2:n], Y[0:n//2,n//2:n]
        C, G = X[n//2:n,0:n//2], Y[n//2:n,0:n//2]
        D, H = X[n//2:n,n//2:n], Y[n//2:n,n//2:n]
        a = self.divideAndConquer(A, E) + self.divideAndConquer(B, G)
        b = self.divideAndConquer(A, F) + self.divideAndConquer(B, H)
        c = self.divideAndConquer(C, E) + self.divideAndConquer(D, G)
        d = self.divideAndConquer(C, F) + self.divideAndConquer(D, H)
        ans = np.vstack((np.hstack((a, b)), np.hstack((c, d))))
        return ans

    def strassen(self, X, Y):
        n = len(X)
        if n < 2:
            return X * Y

        a, e = X[0:n//2,0:n//2], Y[0:n//2,0:n//2]
        b, f = X[0:n//2,n//2:n], Y[0:n//2,n//2:n]
        c, g = X[n//2:n,0:n//2], Y[n//2:n,0:n//2]
        d, h = X[n//2:n,n//2:n], Y[n//2:n,n//2:n]

        p1 = self.strassen(a, f - h)
        p2 = self.strassen(a + b, h)
        p3 = self.strassen(c + d, e)
        p4 = self.strassen(d, g - e)
        p5 = self.strassen(a + d, e + h)
        p6 = self.strassen(b - d, g + h)
        p7 = self.strassen(a - c, e + f)

        c11 = p5 + p4 - p2 + p6
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p1 + p5 - p3 - p7

        c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        return c

np.random.seed(10)
n = 1024
X, Y = np.random.rand(n, n), np.random.rand(n, n)
a = Solutions()

tic = time.time()
i = a.bruteForce(X, Y)
toc = time.time()
print('bruteForce takes ' + str(toc - tic) + ' secs')
j = a.divideAndConquer(X, Y)
tic = time.time()
print('divide&conquer takes ' + str(tic - toc) + ' secs')
k = a.strassen(X, Y)
toc = time.time()
print('strassens takes' + str(toc - tic) + ' secs')


