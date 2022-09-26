# https://leetcode.com/problems/path-sum-ii/

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
        self.paths = []

    def dfs(self, node: Optional[TreeNode], newTgt: int, path: List[int]) -> None:
        if not node:
            return
        if node.val is not None:
            path.append(node.val)
            newTgt -= node.val
            if node.left is None and node.right is None:
                if newTgt == 0:
                    self.paths.append(list(path))
            self.dfs(node.left, newTgt, path)
            self.dfs(node.right, newTgt, path)
            path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root, targetSum, [])
        return self.paths

def main():
    print("*"*25, "Example: 1", "*"*25)
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    target_sum = 22
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    paths = Solution().pathSum(tree[0], target_sum)
    ans = [[5, 4, 11, 2], [5, 8, 4, 5]]
    print(f"Expected Paths: {ans}")
    print(f"Returned Paths: {paths}")
    assert ans == paths, f"Returned Paths {paths} doesn't match with Expected Paths {ans}"

    print("*"*25, "Example: 2", "*"*25)
    root = [1, 2, 3]
    target_sum = 5
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    paths = Solution().pathSum(tree[0], target_sum)
    ans = []
    print(f"Expected Paths: {ans}")
    print(f"Returned Paths: {paths}")
    assert ans == paths, f"Returned Paths {paths} doesn't match with Expected Paths {ans}"

    print("*"*25, "Example: 3", "*"*25)
    root = [1, 2]
    target_sum = 0
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    paths = Solution().pathSum(tree[0], target_sum)
    ans = []
    print(f"Expected Paths: {ans}")
    print(f"Returned Paths: {paths}")
    assert ans == paths, f"Returned Paths {paths} doesn't match with Expected Paths {ans}"

if __name__ == "__main__":
    main()
