from UF import UnionFind
from Grid import Grid
import numpy as np
import pandas as pd
import time

# Percolation problem:
# Given an NxN array of binary values, determine whether the system "percolates"

size = 100
dim = int(size ** 0.5)

data = pd.DataFrame({'prop_open': np.linspace(0, 1, 50)})
percolate_proportions = []

num_iter = 0
percolate_list = []


for p in np.linspace(0, 1, 50):
    num_iter = 0
    percolate_list = []
    while num_iter < 10000:
        # Initialize a new Union find
        test = UnionFind(size + 2)
        # Union first row with "top" and "bottom" roots
        for i in range(dim):
            test.union(i, size)
        for i in range(size - dim, size):
            test.union(i, size + 1)

        # Initialize a new grid for each float in np.linspace
        my_grid = Grid(size, p)
        my_grid.populate()
        arr = my_grid.get_union_indices()
        for a in arr:
            test.union(a[0], a[1])

        percolate_list.append(test.percolates())

        num_iter += 1
    percolate_proportions.append(sum(percolate_list) / len(percolate_list))

data['prop_percolated'] = percolate_proportions
data.to_csv("~/Documents/UM/Fall_2020/DataStructures/Percolation_Data.csv")
