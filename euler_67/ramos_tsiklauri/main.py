import csv
import numpy as np
from node import Node

with open('triangle.txt', 'r') as f:
    triangle = list(csv.reader(f, delimiter=' '))

for row in triangle:
    for _ in range(len(triangle[-1]) - len(row)):
        row.append(0)

triangle = np.array(triangle, dtype='int')

node_matrix = []

for i, row in enumerate(triangle):
    temp = []
    for v, val in enumerate(row):
        temp.append(Node(val, [i,v]))

    node_matrix.append(temp)

node_matrix = np.array(node_matrix)


def dijkstras(node_matrix, node, path_length=59):
    matrix = node_matrix
    current = node
    
    try:
        if node_matrix[node.get_left()].get_value() > node_matrix[node.get_right()].get_value():
            current = node_matrix[node.get_left()]

        else:
            current = node_matrix[node.get_right()]
    
    except IndexError:
        return path_length
    
    dijkstras(node_matrix)
    
    