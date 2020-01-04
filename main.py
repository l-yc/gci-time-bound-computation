#!/usr/bin/env python3
import time
import numpy as np
import matplotlib.pyplot as plt

def multiply(a, b):
    n = len(a)

    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c

data1 = { 'n': [], 'time': [] }
data2 = { 'n': [], 'time': [] }

for n in range(0,300,50):
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)
    #print(multiply(a,b))
    #print(np.dot(a,b))

    s1 = time.time()
    r1 = multiply(a,b)
    e1 = time.time()

    data1['n'].append(n)
    data1['time'].append(e1-s1)

    s2 = time.time()
    r2 = np.dot(a,b)
    e2 = time.time()

    data2['n'].append(n)
    data2['time'].append(e2-s2)

plt.plot('n', 'time', marker='o', data=data1, label='plain python')
plt.plot('n', 'time', marker='^', data=data2, label='numpy')

plt.legend()

plt.xlabel('n')
plt.ylabel('time')
plt.title('Graph of time taken for matrix multiplication against n')

plt.show()
plt.savefig('figure.png')
