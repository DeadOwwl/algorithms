import numpy as np

__slots__ = ['a']


def turtle_way(n, k):
    a = np.zeros((n + 1, n + 1), dtype=np.int32)
    for i in range(n + 1):
        a[i, 0] = 1
        a[i, i] = 1
        for j in range(1, i):
            a[i][j] = (a[i - 1][j - 1] + a[i - 1][j]) % 1000000007
    return a[n][k]


f = open('input.txt')
line = f.readline()
w = open('output.txt', 'w')
n = int(line.split(' ')[0])
m = int(line.split(' ')[1])
w.write(str(turtle_way((m + n - 2) % 1000000007, (m - 1) % 1000000007)))
