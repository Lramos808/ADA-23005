import csv
import numpy as np
from node import Node
from sys import setrecursionlimit as yomama

yomama(5000)

with open('triangle.txt', 'r') as f:
    global triangle
    triangle = list(csv.reader(f, delimiter=' '))

for row in triangle:
    for _ in range(len(triangle[-1]) - len(row)):
        row.append(0)

triangle = np.flip(np.array(triangle, dtype='int'))
print(triangle)

node_matrix = []

for i, row in enumerate(triangle):
    temp = []
    for v, val in enumerate(row):
        temp.append(Node(val, [i,v]))

    node_matrix.append(temp)

# node_matrix = np.flip(np.array(node_matrix))

# print(node_matrix)
