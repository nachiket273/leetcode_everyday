# https://leetcode.com/problems/path-sum/

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
        if node.val is not None:
            if j < len(tree):
                node.left = tree[j]
            j += 1
            if j < len(tree):
                node.right = tree[j]
            j += 1

    return [node for node in tree if node.val is not None]

class Solution:
    def dfs(self, node: Optional[TreeNode], remainingSum:int) -> bool:
        if not node:
            return False
        if not node.left and not node.right and remainingSum == node.val:
            return True
        return self.dfs(node.left, remainingSum-node.val)\
            or self.dfs(node.right, remainingSum-node.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum)

def main():
    print("*"*25, "Example: 1", "*"*25)
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    target_sum = 22
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    sum_exists = Solution().hasPathSum(tree[0], target_sum)
    ans = True
    print(f"Actual Path Exists: {ans}")
    print(f"Prediction if Path Exists: {sum_exists}")
    assert ans == sum_exists, f"Prediction if Path Exists {sum_exists} doesn't "\
        + f"match with Actual Path Exists {ans}"

    print("*"*25, "Example: 2", "*"*25)
    root = [1, 2, 3]
    target_sum = 5
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    sum_exists = Solution().hasPathSum(tree[0], target_sum)
    ans = False
    print(f"Actual Path Exists: {ans}")
    print(f"Prediction if Path Exists: {sum_exists}")
    assert ans == sum_exists, f"Prediction if Path Exists {sum_exists} doesn't "\
        + f"match with Actual Path Exists {ans}"

    print("*"*25, "Example: 3", "*"*25)
    root = []
    target_sum = 0
    print(f"Values: {root}, Target Sum: {target_sum}")
    tree = create_tree(root)
    print("Tree: ")
    for node in tree:
        print(node)
    sum_exists = Solution().hasPathSum(None, target_sum)
    ans = False
    print(f"Actual Path Exists: {ans}")
    print(f"Prediction if Path Exists: {sum_exists}")
    assert ans == sum_exists, f"Prediction if Path Exists {sum_exists} doesn't "\
        + f"match with Actual Path Exists {ans}"

if __name__ == "__main__":
    main()
