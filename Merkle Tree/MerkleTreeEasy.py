#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 07:26:28 2023

@author: cornelius
"""


import hashlib
depth = 2

leaves = [1,2,3,4]

hashed_leaves = \
[hashlib.sha256(str(i).encode()).hexdigest() for i in leaves]
    
tree = []
tree.append(hashed_leaves)
for i in range(0,depth):
    num_leaves = 2**(depth-i)
    new_leaves = []
    for k in range(0,num_leaves,2):
        node1 = hashed_leaves[k]
        node2 = hashed_leaves[k+1]
        new_node = \
            hashlib.sha256((str(node1)+str(node2)).encode()).hexdigest()
        new_leaves.append(new_node)
            
    hashed_leaves = new_leaves
    tree.append(new_leaves)

merkle_tree = list(reversed(tree))
for i in merkle_tree:
    print(i)
    print("\n")
    
    
    
