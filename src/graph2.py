import numpy as np

A = np.matrix([
    [1, 2], [1,3], [1,4], [1,5]
])

x = np.matrix([[1], [1], [1], [1]])

v = x/np.linalg.norm(x) + np.matrix([[1], [0], [0], [0]])
w =2/(np.transpose(v)*v)

print(v)
print(w)
print(np.norm(w))
P1 = np.identity(4) - 2/(np.transpose(v)*v)*np.dot(v,np.transpose(v))