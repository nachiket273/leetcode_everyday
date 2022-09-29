# https://leetcode.com/problems/find-k-closest-elements/

from typing import List

class Solution:
    @classmethod
    def findClosestElements(cls, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[-k:]

        left = 0
        right = len(arr) - k

        while left < right:
            mid = (right + left) >> 1
            if abs(x - arr[mid])  >  abs(arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]

def main():
    print("*"*25, "Example: 1", "*"*25)
    arr = [1, 2, 3, 4, 5]
    k, x = 4, 3
    print(f"Nums: {arr}, x: {x}, k: {k}")
    k_nearest = Solution.findClosestElements(arr, k, x)
    ans = [1, 2, 3, 4]
    print(f"Calculated {k}-nearest nums: {k_nearest}")
    print(f"Expected {k}-nearest nums: {ans}")
    assert ans == k_nearest, f"Calculated {k}-nearest nums: {k_nearest} doesn't"\
        + f" match with Expected {k}-nearest nums: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    arr = [1, 2, 3, 4, 5]
    k, x = 4, -1
    print(f"Nums: {arr}, x: {x}, k: {k}")
    k_nearest = Solution.findClosestElements(arr, k, x)
    ans = [1, 2, 3, 4]
    print(f"Calculated {k}-nearest nums: {k_nearest}")
    print(f"Expected {k}-nearest nums: {ans}")
    assert ans == k_nearest, f"Calculated {k}-nearest nums: {k_nearest} doesn't"\
        + f" match with Expected {k}-nearest nums: {ans}"

if __name__ == "__main__":
    main()
