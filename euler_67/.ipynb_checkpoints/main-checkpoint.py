import csv
import numpy as np

with open('triangle.txt', 'r') as f:
    triangle = list(csv.reader(f, delimiter=' '))

for row in triangle:
    for _ in range(len(triangle[-1]) - len(row)):
        row.append(0)

triangle = np.array(triangle, dtype='int')

print(np.shape(triangle))