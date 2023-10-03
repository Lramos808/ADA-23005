import csv
import numpy as np

with open('matrix.txt', 'r') as f:
    matrix = np.array(list(csv.reader(f, delimiter=',')), dtype='int')

print(matrix)