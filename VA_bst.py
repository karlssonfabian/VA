"""
Solutions to module VA bst

Student:
Mail:
"""
import random as r
import numpy as np
import math as m

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)
    
    def ipl(self):
        def _ipl(n, depth):
            if n is None:
                return 0
            return depth + _ipl(n.left, depth+1) + _ipl(n.right, depth+1)
        return _ipl(self.root, 1)
        
    def height(self):
        def _height(n):
            if n is None:
                return 0
            height_left = _height(n.left)
            height_right = _height(n.right)
            return 1 + max(height_left, height_right)
        return _height(self.root)

def random_tree(n):                               # Useful
    t = BST()
    for _ in range(n):
        t.insert(round(r.random(), 3))
    return t

def experiment():
    for k in range(1, 10):
        n = 1000 * 2**k
        theoretical_ipl = 1.39*n*np.log2(n)
        
        t = random_tree(n)
        
        ipl = t.ipl()
        ipl_avg = ipl / n
        height = t.height()
        
        print('-'*40)
        print(f'n = {n}')
        print(f'Observed IPL / n: {ipl_avg}')
        print(f'Observed IPL: {ipl}')
        print(f'Theoretical IPL: {theoretical_ipl}')
        print(f'Height: {height}')
        
        
    

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()
    #print(t.ipl())
    t = random_tree(11)
    t.print()
    print()
    print(t.ipl())
    experiment()
    


if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?

What can you guess about the
height?

"""
