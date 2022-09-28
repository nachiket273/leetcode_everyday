# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @classmethod
    def removeNthFromEnd(cls, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

def create_linkedlist(nums: List[int]) ->  Optional[ListNode]:
    head = ListNode(nums[0])
    prev = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        prev.next = node
        prev = node

    return head

def display_llist(node: Optional[ListNode]) -> None:
    print("LinkedList: ")
    llist = ""
    while node:
        llist += str(node.val)
        if node.next:
            llist += " -> "
        node = node.next

    print(llist)

def llist_to_list(node: Optional[ListNode]) -> List[int]:
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums

def main():
    print("*"*25, "Example: 1", "*"*25)
    head = [1, 2, 3, 4, 5]
    llist = create_linkedlist(head)
    display_llist(llist)
    n = 2
    print(f"Remove {n}th element from list.")
    new_llist = Solution.removeNthFromEnd(llist, n)
    new_list = llist_to_list(new_llist)
    ans = [1, 2, 3, 5]
    print(f"Returned LinkedList: {new_list}")
    print(f"Expected LinkedList: {ans}")
    assert ans == new_list, f"Returned LinkedList {new_list} doesn't"\
        + f" match with Expected LinkedList {ans}"

    print("*"*25, "Example: 2", "*"*25)
    head = [1]
    llist = create_linkedlist(head)
    display_llist(llist)
    n = 1
    print(f"Remove {n}th element from list.")
    new_llist = Solution.removeNthFromEnd(llist, n)
    new_list = llist_to_list(new_llist)
    ans = []
    print(f"Returned LinkedList: {new_list}")
    print(f"Expected LinkedList: {ans}")
    assert ans == new_list, f"Returned LinkedList {new_list} doesn't"\
        + f" match with Expected LinkedList {ans}"

    print("*"*25, "Example: 3", "*"*25)
    head = [1, 2]
    llist = create_linkedlist(head)
    display_llist(llist)
    n = 1
    print(f"Remove {n}th element from list.")
    new_llist = Solution.removeNthFromEnd(llist, n)
    new_list = llist_to_list(new_llist)
    ans = [1]
    print(f"Returned LinkedList: {new_list}")
    print(f"Expected LinkedList: {ans}")
    assert ans == new_list, f"Returned LinkedList {new_list} doesn't"\
        + f" match with Expected LinkedList {ans}"

if __name__ == "__main__":
    main()
    