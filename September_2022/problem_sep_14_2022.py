# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

from collections import defaultdict
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
    def __init__(self):
        self.count = 0
        self.path = defaultdict(int)

    def is_psuedo_palindrome(self) -> bool:
        is_odd = False

        for val in self.path.values():
            if val % 2 == 1:
                if is_odd:
                    return False
                is_odd = True
        return True

    def preorder(self, node: Optional[TreeNode]) -> None:
        if node:
            self.path[node.val] += 1

            if node.left is None and node.right is None:
                if self.is_psuedo_palindrome():
                    self.count += 1

            self.preorder(node.left)
            self.preorder(node.right)
            self.path[node.val] -= 1

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.preorder(root)
        return self.count

def main():
    print("*"*25, "Example: 1", "*"*25)
    root = [2, 3, 1, 3, 1, None, 1]
    print(f"Values: {root}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    soln = Solution()
    count = soln.pseudoPalindromicPaths(tree[0])
    ans = 2
    print(f"Expected Psuedopalindrome Count: {ans}")
    print(f"Returned Psuedopalindrome Count: {count}")
    assert count == ans, f"Returned Psuedopalindrome Count {count}"\
        + f" doesn't match with Expected Psuedopalindrome Count {ans}"

    print("*"*25, "Example: 2", "*"*25)
    root = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
    print(f"Values: {root}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    soln = Solution()
    count = soln.pseudoPalindromicPaths(tree[0])
    ans = 1
    print(f"Expected Psuedopalindrome Count: {ans}")
    print(f"Returned Psuedopalindrome Count: {count}")
    assert count == ans, f"Returned Psuedopalindrome Count {count}"\
        + f" doesn't match with Expected Psuedopalindrome Count {ans}"

if __name__ == "__main__":
    main()
