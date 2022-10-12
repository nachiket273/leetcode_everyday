# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List

class Solution:
    @classmethod
    def increasingTriplet(cls, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num < first:
                first = num
            elif first < num and num < second:
                second = num
            elif second < num:
                return True

        return False

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 2, 3, 4, 5]
    print(f"Numbers: {nums}")
    res = Solution.increasingTriplet(nums)
    ans = True
    print(f"Increasing Triplet Subsequence Exists: {ans}")
    print(f"Calculated if Increasing Triplet Subsequence Exists: {res}")
    assert ans == res, f"Increasing Triplet Subsequence Exists {res} "\
        + f"doesn't match with Calculated if Increasing Triplet Subsequence Exists {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [5, 4, 3, 2, 1]
    print(f"Numbers: {nums}")
    res = Solution.increasingTriplet(nums)
    ans = False
    print(f"Increasing Triplet Subsequence Exists: {ans}")
    print(f"Calculated if Increasing Triplet Subsequence Exists: {res}")
    assert ans == res, f"Increasing Triplet Subsequence Exists {res} "\
        + f"doesn't match with Calculated if Increasing Triplet Subsequence Exists {ans}"

if __name__ == "__main__":
    main()
