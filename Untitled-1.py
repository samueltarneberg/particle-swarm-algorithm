import numpy as np
x_pb = [[1,2],[2,3]]
r = [[2],[3]]
g = [r*2 for r in r ]

print(np.shape(g))
a = np.array([[0.1,0.1],[0.1,0.1]])
b = np.array([[1,1],[1,1]])
c = a*b


