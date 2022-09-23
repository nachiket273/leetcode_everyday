# https://leetcode.com/problems/average-of-levels-in-binary-tree/
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
    def averageOfLevels(cls, root: Optional[TreeNode]) -> List[float]:
        queue, avg = [], []
        queue.append(root)
        while len(queue) > 0:
            sum_tmp = 0
            num = len(queue)
            for _ in range(num):
                node = queue.pop(0)
                sum_tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sum_tmp = sum_tmp / num
            avg.append(sum_tmp)    
        return avg

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
    avg = Solution.averageOfLevels(tree[0])
    ans = [3.00000,14.50000,11.00000]
    print(f"Expected Averages: {ans}")
    print(f"Returned Averages: {avg}")
    assert ans == avg, f"Output {avg} doesn't match with answer {ans}"

    print("*"*25, "Example: 2", "*"*25)
    vals1 = [3, 9, 20, 15, 7]
    print(f"Values: {vals1}")
    tree1 = create_tree(vals1)
    print("Tree: ")
    for node in tree1:
        print(node)
    avg1 = Solution.averageOfLevels(tree1[0])
    ans1 = [3.00000,14.50000,11.00000]
    print(f"Expected Averages: {ans1}")
    print(f"Returned Averages: {avg1}")
    assert ans1 == avg1, f"Output {avg1} doesn't match with answer {ans1}"

if __name__ == "__main__":
    main()
