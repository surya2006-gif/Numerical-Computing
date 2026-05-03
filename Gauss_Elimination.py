import numpy as np

A = np.array([[2.0, -1.0, 1.0],
              [3.0, 3.0, 9.0],
              [3.0, 3.0, 5.0]])

b = np.array([2.0, -1.0, 4.0])

n = len(b)

for i in range(n):
    for j in range(i+1, n):
        ratio = A[j][i] / A[i][i]
        A[j] = A[j] - ratio * A[i]
        b[j] = b[j] - ratio * b[i]

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (b[i] - sum(A[i][j]*x[j] for j in range(i+1, n))) / A[i][i]

print("Solution:", x)
