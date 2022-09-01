# https://leetcode.com/problems/count-good-nodes-in-binary-tree
import math


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        str1 = f"Current Node Value: {self.val}"
        if self.left:
            str1 += f", Left Node: {self.left.val}"
        else:
            str1 += ", Left Node: None"
        if self.right:
            str1 += f", Right Node: {self.right.val}"
        else:
            str1 += ", Right Node: None"
        return str1


class Solution:
    def __init__(self) -> None:
        self.count = 0

    def dfs(self, node: TreeNode, curmax: int) -> None:
        if not node:
            return

        if node.val >= curmax:
            curmax = node.val
            self.count += 1

        self.dfs(node.left, curmax)
        self.dfs(node.right, curmax)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.count

        curmax = -math.inf
        self.dfs(root, curmax)
        return self.count

def create_tree(vals: list[int]) -> list[TreeNode]:
    tree = [TreeNode(i) for i in vals]
    j = 1
    for i, node in enumerate(tree):
        if j < len(tree):
            if tree[j].val is not None:
                node.left = tree[j]
        j += 1
        if j < len(tree):
            if tree[j].val is not None:
                node.right = tree[j]
        j += 1

    return [node for node in tree if node.val is not None]

def main():
    print("*"*25, "Example: 1", "*"*25)
    vals = [3, 1, 4, 3, None, 1, 5]
    print(f"Values: {vals}")
    tree = create_tree(vals)
    print("Tree: ")
    for node in tree:
        print(node)
    soln = Solution()
    count = soln.goodNodes(tree[0])
    print("Expected Count: 4")
    print(f"Returned Count: {count}")
    assert count == 4, f"Output {count} doesn't match with answer 4"

    print("*"*25, "Example: 2", "*"*25)
    vals1 = [3, 3, None, 4, 2]
    print(f"Values: {vals1}")
    tree1 = create_tree(vals1)
    print("Tree: ")
    for node in tree1:
        print(node)
    soln = Solution()
    count1 = soln.goodNodes(tree1[0])
    print("Expected Count: 3")
    print(f"Returned Count: {count1}")
    assert count1 == 3, f"Output {count1} doesn't match with answer 3"

if __name__ == "__main__":
    main()
