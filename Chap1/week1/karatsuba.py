import time
def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(m2 *2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)
def gradeschool(x, y):
    X, Y = str(x), str(y)
    m, n = len(X), len(Y)
    Z = [0 for i in range(m + n)]
    z = 0
    for i in range(m - 1, -1, -1):
        for j in range(n -1, -1, -1):
            product = int(X[i]) * int(Y[j])
            Z[i + j + 1] += product % 10
            Z[i + j] += product // 10
    for i in range(m + n - 1):
        z += Z[i]
        z *= 10
    z += Z[m + n - 1]
    return z

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

a = time.time()
z1 = karat(x, y)
t1 = time.time() - a
print('karatsuba: ' + str(t1))

a = time.time()
z2 = x * y
t1 = time.time() - a
print('python: ' + str(t1))

a = time.time()
z3 = gradeschool(x, y)
t1 = time.time() - a
print('gradeschool: ' + str(t1))


print(z3)
print(z3 == z2)