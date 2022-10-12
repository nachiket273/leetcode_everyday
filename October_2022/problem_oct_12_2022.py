# https://leetcode.com/problems/largest-perimeter-triangle/

from typing import List

class Solution:
    @classmethod
    def largestPerimeter(cls, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i+2] + nums[i+1] > nums[i]:
                 return nums[i] + nums[i+1] + nums[i+2]
        return 0

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [2, 1, 2]
    print(f"Numbers: {nums}")
    res = Solution.largestPerimeter(nums)
    ans = 5
    print(f"Largest Perimeter Triangle: {ans}")
    print(f"Calculated Largest Perimeter Triangle: {res}")
    assert ans == res, f"Largest Perimeter Triangle {res} "\
        + f"doesn't match with Calculated Largest Perimeter Triangle {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [1, 2, 1]
    print(f"Numbers: {nums}")
    res = Solution.largestPerimeter(nums)
    ans = 0
    print(f"Largest Perimeter Triangle: {ans}")
    print(f"Calculated Largest Perimeter Triangle: {res}")
    assert ans == res, f"Largest Perimeter Triangle {res} "\
        + f"doesn't match with Calculated Largest Perimeter Triangle {ans}"

if __name__ == "__main__":
    main()
