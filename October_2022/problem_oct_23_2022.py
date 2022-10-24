# https://leetcode.com/problems/set-mismatch/

from typing import List

class Solution:
    @classmethod
    def findErrorNums(cls, nums: List[int]) -> List[int]:
        ans = [-1, -1]
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans[0] = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                ans[1] = i+1

        return ans

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 2, 2, 4]
    print(f"Nums: {nums}")
    missing = Solution.findErrorNums(nums)
    ans = [2, 3]
    print(f"Calculated duplicate and repeated numbers: {missing}")
    print(f"Actual duplicate and repeated numbers: {ans}")
    assert missing == ans, f"Calculated duplicate and repeated numbers: {missing} "\
        + f"doesn't match with Actual duplicate and repeated numbers: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [1, 1]
    print(f"Nums: {nums}")
    missing = Solution.findErrorNums(nums)
    ans = [1, 2]
    print(f"Calculated duplicate and repeated numbers: {missing}")
    print(f"Actual duplicate and repeated numbers: {ans}")
    assert missing == ans, f"Calculated duplicate and repeated numbers: {missing} "\
        + f"doesn't match with Actual duplicate and repeated numbers: {ans}"

if __name__ == "__main__":
    main()
