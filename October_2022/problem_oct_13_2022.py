# https://leetcode.com/problems/delete-node-in-a-linked-list/

from typing import List

class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None

def create_ll(nums: List) -> ListNode:
    head = ListNode(nums[0])
    prev = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        prev.next = node
        prev = node

    return head

def get_ll(head: ListNode) -> List:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next

    return nums

class Solution:
    @classmethod
    def deleteNode(cls, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

def main():
    print("*"*25, "Example: 1", "*"*25)
    head = [4, 5, 1, 9]
    node = 5
    print(f"List: {head}")
    print(f"Node to be deleted: {node}")
    first = create_ll(head)
    lst = first
    while lst.val != node:
        lst = lst.next
    Solution.deleteNode(lst)
    new_lst = get_ll(first)
    ans = [4, 1, 9]
    print(f"List after node deletion: {new_lst}")
    assert new_lst == ans, f"Calculated List after node deletion {new_lst} "\
        + f"doesn't match with List after node deletion {ans}"

    print("*"*25, "Example: 2", "*"*25)
    head = [4, 5, 1, 9]
    node = 1
    print(f"List: {head}")
    print(f"Node to be deleted: {node}")
    first = create_ll(head)
    lst = first
    while lst.val != node:
        lst = lst.next
    Solution.deleteNode(lst)
    new_lst = get_ll(first)
    ans = [4, 5, 9]
    print(f"List after node deletion: {new_lst}")
    assert new_lst == ans, f"Calculated List after node deletion {new_lst} "\
        + f"doesn't match with List after node deletion {ans}"

if __name__ == "__main__":
    main()
