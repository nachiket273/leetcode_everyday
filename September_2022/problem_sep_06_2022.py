# https://leetcode.com/problems/binary-tree-pruning/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def should_keep(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return False

        left_prune = self.should_keep(node.left)
        right_prune = self.should_keep(node.right)

        if not left_prune:
            node.left = None

        if not right_prune:
            node.right = None

        return node.val or left_prune or right_prune

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.should_keep(root):
            return root
        return None
