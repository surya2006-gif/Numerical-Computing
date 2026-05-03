import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 4, 8])

n = len(x)
diff = np.zeros((n, n))
diff[:,0] = y

for j in range(1, n):
    for i in range(n-j):
        diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

value = 1.5
h = x[1] - x[0]
u = (value - x[0]) / h

result = y[0]
u_term = 1

for i in range(1, n):
    u_term *= (u - (i-1)) / i
    result += u_term * diff[0][i]

print("Interpolated value:", result)
