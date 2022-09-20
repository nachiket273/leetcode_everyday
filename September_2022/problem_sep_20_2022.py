# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List

class Solution:
    @classmethod
    def findLength(cls, nums1: List[int], nums2: List[int]) -> int:
        n_1, n_2 = len(nums1), len(nums2)
        d_p = [[0 for _ in range(n_2+1)] for _ in range(n_1+1)]

        for i in range(n_1-1, -1, -1):
            for j in range(n_2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    d_p[i][j] = d_p[i+1][j+1] + 1

        return max([max(i) for i  in d_p])

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print(f"Arrays: nums1: {nums1}, nums2: {nums2}")
    max_len = Solution.findLength(nums1, nums2)
    ans = 3
    print(f"Expected max length of substring: {ans}")
    print(f"Calculated max length of substring: {max_len}")
    assert ans == max_len, f"Calculated max length of substring {max_len} doesn't"\
                            + f" match with Expected max length of substring {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums1 = [0, 0, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 0]
    print(f"Arrays: nums1: {nums1}, nums2: {nums2}")
    max_len = Solution.findLength(nums1, nums2)
    ans = 5
    print(f"Expected max length of substring: {ans}")
    print(f"Calculated max length of substring: {max_len}")
    assert ans == max_len, f"Calculated max length of substring {max_len} doesn't"\
                            + f" match with Expected max length of substring {ans}"

if __name__ == "__main__":
    main()
