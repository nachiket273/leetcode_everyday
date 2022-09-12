# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
from collections import defaultdict
from typing import Optional, List


class TreeNode:
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
    @classmethod
    def verticalTraversal(cls, root: Optional[TreeNode]) -> List[List[int]]:
        ans= []

        def dfs(node, row, col):
            if node:
                ans.append([row, col, node.val])
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)

        dfs(root, 0, 0)
        ans = sorted(ans, key= lambda k: (k[1], k[0], k[2]))

        d = defaultdict(list)
        for val in ans:
            d[val[1]].append(val[2])

        return [val for val in d.values()]

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
    vals = [3, 9, 20, None, None, 15, 7]
    print(f"Values: {vals}")
    tree = create_tree(vals)
    print("Tree: ")
    for node in tree:
        print(node)
    res = Solution.verticalTraversal(tree[0])
    ans = [[9], [3, 15], [20], [7]]
    print(f"Expected Answer: {ans}")
    print(f"Result: {res}")
    assert ans == res, f"Output {res} doesn't match with answer {ans}"

    print("*"*25, "Example: 2", "*"*25)
    vals = [1, 2, 3, 4, 5, 6, 7]
    print(f"Values: {vals}")
    tree = create_tree(vals)
    print("Tree: ")
    for node in tree:
        print(node)
    res = Solution.verticalTraversal(tree[0])
    ans = [[4], [2], [1, 5, 6], [3], [7]]
    print(f"Expected Answer: {ans}")
    print(f"Result: {res}")
    assert ans == res, f"Output {res} doesn't match with answer {ans}"

if __name__ == "__main__":
    main()
