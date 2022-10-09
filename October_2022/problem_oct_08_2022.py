# https://leetcode.com/problems/3sum-closest/

from typing import List

class Solution:
    @classmethod
    def threeSumClosest(cls, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        closest = float("inf")
        for i, num in enumerate(nums):
            low = i+1
            high = len(nums) -1
            while low < high:
                sm = num + nums[low] + nums[high]
                if abs(target-sm) < diff:
                    diff = abs(target-sm)
                    closest = sm
                if sm < target:
                    low += 1
                elif sm > target:
                    high -= 1
                else:
                    return sm
                    
        return closest

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [-1, 2, 1, -4]
    target = 1
    print(f"Nums: {nums}, target: {target}")
    closest = Solution.threeSumClosest(nums, target)
    ans = 2
    print(f"Expected closest sum: {ans}")
    print(f"Calculated closest sum: {closest}")
    assert ans == closest, f"Calculated closest sum {closest} "\
        + f"doesn't match with Expected closest sum {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [0, 0, 0]
    target = 1
    print(f"Nums: {nums}, target: {target}")
    closest = Solution.threeSumClosest(nums, target)
    ans = 0
    print(f"Expected closest sum: {ans}")
    print(f"Calculated closest sum: {closest}")
    assert ans == closest, f"Calculated closest sum {closest} "\
        + f"doesn't match with Expected closest sum {ans}"

if __name__ == "__main__":
    main()