# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional

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
    if len(vals) == 0:
        return [TreeNode(None)]
    tree = [TreeNode(i) for i in vals]
    j = 1
    for i, node in enumerate(tree):
        if node.val is not None:
            if j < len(tree):
                node.left = tree[j]
            j += 1
            if j < len(tree):
                node.right = tree[j]
            j += 1

    return [node for node in tree if node.val is not None]

class Solution:
    def __init__(self):
        self.ret = []

    def dfs(self, node: Optional[TreeNode]) -> None:
        if node and node.val:
            self.dfs(node.left)
            self.ret.append(node.val)
            self.dfs(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.ret

def main():
    print("*"*25, "Example: 1", "*"*25)
    root = [1, None, 2, 3]
    print(f"Values: {root}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    out = Solution().inorderTraversal(tree[0])
    ans = [1, 3, 2]
    print(f"Expected Inorder Traversal: {ans}")
    print(f"Returned Inorder Traversal: {out}")
    assert ans == out, f"Returned Inorder Traversal {out}"\
        + f" doesn't match with Expected Inorder Traversal {ans}"

    print("*"*25, "Example: 2", "*"*25)
    root = []
    print(f"Values: {root}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    out = Solution().inorderTraversal(tree[0])
    ans = []
    print(f"Expected Inorder Traversal: {ans}")
    print(f"Returned Inorder Traversal: {out}")
    assert ans == out, f"Returned Inorder Traversal {out}"\
        + f" doesn't match with Expected Inorder Traversal {ans}"

    print("*"*25, "Example: 3", "*"*25)
    root = [1]
    print(f"Values: {root}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    out = Solution().inorderTraversal(tree[0])
    ans = [1]
    print(f"Expected Inorder Traversal: {ans}")
    print(f"Returned Inorder Traversal: {out}")
    assert ans == out, f"Returned Inorder Traversal {out}"\
        + f" doesn't match with Expected Inorder Traversal {ans}"

if __name__ == "__main__":
    main()
