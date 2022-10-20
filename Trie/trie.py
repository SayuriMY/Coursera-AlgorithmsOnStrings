# Uses python3
"""
File name: trie.py
Author: Sayuri Monarrez Yesaki
Date created: 10/19/2022
Date last modified: 10/19/2022
Python version: 3.9

Task: Construct a trie from a collection of patterns.

Input: An integer n and a collection of strings Patterns = {p1, ..., pn} (each string is given on a separate line).

Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖’s contain only symbols A, C, G, T; no 𝑝𝑖 is a prefix
            of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.

Output: The adjacency list corresponding to Trie(Patterns), in the following format:
        - If Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with the integers
        1 through n-1 in any order you like.
        - Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple:
            --> the first two members of the triple must be the integers i, j, labeling the initial and terminal nodes
            of the edge, respectively;
            --> the third member of the triple must be the symbol c labeling the edge;
        output each such triple in the format u -> v:c (with no space) on a separate line.

Time limit: 2 sec

Memory Limit: 512 MB
"""

import sys


def build_trie(patterns):
    """
    Return the trie built from patterns in the form of a dictionary of dictionaries,
        e.g. {
                0:{'A':1,'T':2},
                1:{'C':3}
            }
    where the key of the external dictionary is the node ID (integer), and the internal dictionary contains all the
    trie edges outgoing from the corresponding node, and the keys are the letters on those edges, and the values
    are the node IDs to which these edges lead.
    """
    tree = dict()
    # write your code here
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
