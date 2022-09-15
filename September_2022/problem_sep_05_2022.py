# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from collections import defaultdict
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.lvl = defaultdict(list)

    def dfs(self, node: 'Node', level: int) -> None:
        if not node:
            return
        self.lvl[level].append(node.val)
        for child in node.children:
            self.dfs(child, level+1)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.dfs(root, 0)
        return [lst for _, lst in self.lvl.items()]
