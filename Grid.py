import numpy as np
from pprint import pprint


# Binary grid object


class Grid:
    def __init__(self, dim, proportion):
        self.dim = dim
        self.proportion = proportion

        # Requires Square dimensionality
        self.edge_size = int(dim ** 0.5)
        self.grid = [[0 for x in range(self.edge_size)] for y in range(self.edge_size)]
        self.cells = [[i, j] for i in range(0, self.edge_size) for j in range(0, self.edge_size)]

    def populate(self):
        for i in range(self.edge_size):
            for j in range(self.edge_size):
                random = np.random.rand()
                if random < self.proportion:
                    self.grid[i][j] = 1

    def display_grid(self):
        pprint(self.grid)

    def to_1d(self, coord):
        return self.edge_size * coord[0] + coord[1]

    def inside(self, i, j):
        if i < 0 or j < 0:
            return False

        elif i > self.dim - 1 or j > self.dim - 1:
            return False

        else:
            return True

    def get_adjacent_cells(self, x_coord, y_coord):
        result = []
        first_order = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for x, y in [(x_coord + i, y_coord + j) for (i, j) in first_order]:

            # Ensure that only 1st order neighborhood cells get chosen
            if [x, y] in self.cells:
                result.append([x, y])

        return result

    def get_union_indices(self):
        arr = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # If "open"
                if self.grid[i][j] == 1:
                    # Check get adjacent cell coordinates
                    adj = self.get_adjacent_cells(i, j)

                    # Iterate over each adjacent cell coordinate
                    for a in adj:
                        x = a[0]
                        y = a[1]

                        # and check if each adjacent cell is a 1
                        if self.grid[x][y] == 1:
                            # Convert the 2 dimensional coordinate to 1d UF-readable format
                            uf_index_adjacent = self.to_1d(a)
                            uf_index_i_j = self.to_1d([i, j])
                            arr.append([uf_index_i_j, uf_index_adjacent])

        # Remove duplicates -- Not needed- faster for Union Find to catch anyhow
        # b = []
        # for aa in arr:
        #     if not any([set(aa) == set(bb) for bb in b if len(aa) == len(bb)]):
        #         b.append(aa)
        return arr
