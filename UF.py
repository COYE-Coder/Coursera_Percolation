# Even smarter still!
# Implementation of Union Find- uses the "Weighted Union" algorithm

class UnionFind:
    # First define a data structure
    def __init__(self, size):
        self.size = size
        self.two_dim = False
        self.d_structure = [i for i in range(size)]
        self.tree_sizes = [1] * self.size

    def is_connected(self, p, q):
        return self.get_root(p) == self.get_root[q]

    def get_root(self, p):
        while self.d_structure[p] != p:
            p = self.d_structure[p]

            # "Path Compression Improvement:
            self.d_structure[p] = self.d_structure[self.d_structure[p]]
        return p

    def union(self, p, q):
        root_p = self.get_root(p)
        root_q = self.get_root(q)

        # Always set smaller tree to larger tree's root
        if self.tree_sizes[root_p] > self.tree_sizes[root_q]:
            self.d_structure[root_q] = root_p

            # Increase sizes of the root "tree"
            self.tree_sizes[root_p] += self.tree_sizes[root_q]

        else:
            self.d_structure[root_p] = root_q
            self.tree_sizes[root_q] += self.tree_sizes[root_p]

    def display(self):
        print("Data Structure: ")
        print(self.d_structure)
        print("Tree Sizes: ")
        print(self.tree_sizes)

    def percolates(self):
        return self.get_root(self.size - 2) == self.get_root(self.size - 1)