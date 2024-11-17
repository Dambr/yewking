import numpy as np
from random import randint

m = 4
k = 3
dtype = np.int64

A_bin = np.zeros((m, k), dtype=dtype)
A_dis = np.zeros((m, k), dtype=dtype)
X_bin = np.zeros(m * k, dtype=dtype)
X_dis = np.zeros(m, dtype=dtype)

for i in range(m * k):
	X_bin[i] = i + 1

for i in range(m):
	X_dis[i] = randint(0, k)

print('X_bin', X_bin)
print('X_dis', X_dis)

def get_bin(i, j):
	index = i * k - (k - j)
	return X_bin[index - 1]

for i in range(m):
	for j in range(k):
		A_bin[i][j] = get_bin(i + 1, j + 1)

print('A_bin')
print(A_bin)
