#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:30:03 2025

@author: cornelius
"""

import hashlib

class MerkleTree:
    def __init__(self, data_blocks):
        """
        Initialize the Merkle Tree with a list of data blocks.

        :param data_blocks: List of data blocks (strings) to be included in the tree.
        """
        self.data_blocks = data_blocks
        self.tree = []
        if data_blocks:
            self.build_tree()

    def hash(self, data):
        """
        Generate a SHA-256 hash for the given data.

        :param data: Data to be hashed (string).
        :return: Hexadecimal hash value (string).
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self):
        """
        Build the Merkle Tree from the data blocks.
        """
        # Hash the initial data blocks
        current_level = [self.hash(block) for block in self.data_blocks]
        self.tree.append(current_level)

        # Iteratively build the tree by hashing pairs of nodes
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                if i + 1 < len(current_level):
                    # Hash two adjacent nodes
                    combined_hash = self.hash(current_level[i] + current_level[i + 1])
                else:
                    # Handle odd number of nodes by duplicating the last one
                    combined_hash = self.hash(current_level[i] + current_level[i])
                next_level.append(combined_hash)
            self.tree.append(next_level)
            current_level = next_level

    def get_root(self):
        """
        Get the root hash of the Merkle Tree.

        :return: Root hash of the tree (string), or None if the tree is empty.
        """
        return self.tree[-1][0] if self.tree else None

    def get_proof(self, index):
        """
        Generate a Merkle proof for a given data block index.

        :param index: Index of the data block in the original list.
        :return: List of hashes needed to verify the block.
        """
        if index < 0 or index >= len(self.data_blocks):
            raise IndexError("Index out of range")

        proof = []
        for level in self.tree[:-1]:
            # Determine the sibling index
            if index % 2 == 0:  # Left node
                sibling_index = index + 1 if index + 1 < len(level) else index
            else:  # Right node
                sibling_index = index - 1

            # Add the sibling hash to the proof
            proof.append(level[sibling_index])
            index //= 2

        return proof

    def verify_proof(self, proof, target_hash, root_hash):
        """
        Verify a Merkle proof against a given root hash.

        :param proof: List of hashes needed to verify the block.
        :param target_hash: Hash of the data block being verified (string).
        :param root_hash: Root hash of the Merkle Tree (string).
        :return: True if the proof is valid, False otherwise.
        """
        current_hash = target_hash
        for sibling_hash in proof:
            # Combine the current hash with the sibling hash and re-hash
            if current_hash < sibling_hash:
                current_hash = self.hash(current_hash + sibling_hash)
            else:
                current_hash = self.hash(sibling_hash + current_hash)

        return current_hash == root_hash

# Example usage:
data = ["block1", "block2", "block3", "block4"]
merkle_tree = MerkleTree(data)

print("Merkle Root:", merkle_tree.get_root())

# Generate a proof for the first block
proof = merkle_tree.get_proof(0)
print("Proof for block1:", proof)

# Verify the proof
block_hash = merkle_tree.hash("block1")
is_valid = merkle_tree.verify_proof(proof, block_hash, merkle_tree.get_root())
print("Is the proof valid?", is_valid)
