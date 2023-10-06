import csv
import numpy as np
from node import Node
from sys import setrecursionlimit

setrecursionlimit(10000)

with open('triangle.txt', 'r') as f:
    global triangle
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

global path_sums
path_sums = []

def dijkstras(node_matrix, node=node_matrix[0,0], path_list=[[0,0]], up_count=0):
    node_matrix = node_matrix
    current = node
    path_list = path_list
    
    temp = []
    for index in path_list:
        temp.append(node_matrix[index[0], index[1]].get_value())
    if current.get_highest_sum() < sum(temp):
        current.set_highest_sum(sum(temp))
    else:
        current.set_no_go(True)
        path_list.pop()
        current = node_matrix[path_list[-1][0], path_list[-1][1]]
        

    
    if current.get_index()[0] == 99:
        temp = []
        for index in path_list:
            temp.append(node_matrix[index[0], index[1]].get_value())
        path_sums.append(sum(temp))
        up_count = 0
        current.set_no_go(True)
        current = node_matrix[path_list[-2][0], path_list[-2][1]]
        path_list.pop()
    
    elif node_matrix[current.get_left()].get_no_go() and not node_matrix[current.get_right()].get_no_go():
        
        current = node_matrix[current.get_right()]
        path_list.append(current.get_index())
        up_count = 0
    
    elif not node_matrix[current.get_left()].get_no_go() and node_matrix[current.get_right()].get_no_go():
        
        current = node_matrix[current.get_left()]
        path_list.append(current.get_index())
        up_count = 0
    
    elif not node_matrix[current.get_left()].get_no_go() and not node_matrix[current.get_right()].get_no_go():
        current = node_matrix[current.get_left()] if node_matrix[current.get_left()].get_value() >= node_matrix[current.get_right()].get_value() else node_matrix[current.get_right()]
        path_list.append(current.get_index())
    
    elif node_matrix[current.get_left()].get_no_go() and node_matrix[current.get_right()].get_no_go():
        current.set_no_go(True)
        path_list.pop()
        current = node_matrix[path_list[-1][0], path_list[-1][1]]
        for value in node_matrix[(current.get_index()[0]) + 2]:
            value.set_no_go(False)

    print(path_list)
    # print(node_matrix[path_list[-1]].get_no_go())
    # if len(path_sums) > 0:
    #     print(sorted(path_sums, reverse=True))

    dijkstras(node_matrix, current, path_list)

dijkstras(node_matrix)
