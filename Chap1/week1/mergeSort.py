def mergeOrderedList(x, y):
    m, n = len(x), len(y)
    i, j = 0, 0
    z = []
    for k in range(m + n):
        if i == m:
            z.extend(y[j:n])
            break
        elif j == n:
            z.extend(x[i:m])
            break
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z
def merge(x):
    n = len(x)
    if n <= 1:
        return x
    return mergeOrderedList(merge(x[0:n//2]), merge(x[n//2: n]))



x = [1,45,2,5,7,23,2,3,57,37,4,8]
z = merge(x)
print(z)
