# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional

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

class Solution:
    def __init__(self) -> None:
        self.flg = False
        self.nums = set()

    def traverse(self, node, tgt) -> None:
        if not node:
            return

        if tgt - node.val in self.nums:
            self.flg = True
            return

        self.nums.add(node.val)
        if node.left:
            self.traverse(node.left, tgt)

        if node.right:
            self.traverse(node.right, tgt)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.traverse(root, k)
        return self.flg

def main():
    print("*"*25, "Example: 1", "*"*25)
    root = [5, 3, 6,  2, 4, None, 7]
    k = 9
    print(f"Values: {root}, sum: {k}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    res = Solution().findTarget(tree[0], k)
    ans = True
    print(f"Expected Answer: {ans}")
    print(f"Result: {res}")
    assert ans == res, f"Output {res} doesn't match with answer {ans}"

    print("*"*25, "Example: 2", "*"*25)
    root = [5, 3, 6, 2, 4, None, 7]
    k = 28
    print(f"Values: {root}, sum: {k}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    res = Solution().findTarget(tree[0], k)
    ans = False
    print(f"Expected Answer: {ans}")
    print(f"Result: {res}")
    assert ans == res, f"Output {res} doesn't match with answer {ans}"

if __name__ == "__main__":
    main()
