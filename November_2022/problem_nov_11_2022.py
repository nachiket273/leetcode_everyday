# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    @classmethod
    def removeDuplicates(cls, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j-1]
                i += 1
        nums[i] = nums[-1]
        
        return i+1

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 1, 2]
    print(f"Numbers: {nums}")
    idx = Solution.removeDuplicates(nums)
    ans = 2
    print(f"Calculated array without adjacent duplicates: {nums[:idx]}")
    print(f"Actual array without adjacent duplicates: {nums[:ans]}")
    assert nums[:idx] == nums[:ans], f"Calculated array without adjacent duplicates: {nums[:idx]} doesn't match"\
                       f"Actual array without adjacent duplicates: {nums[:ans]}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Numbers: {nums}")
    idx = Solution.removeDuplicates(nums)
    ans = 5
    print(f"Calculated array without adjacent duplicates: {nums[:idx]}")
    print(f"Actual array without adjacent duplicates: {nums[:ans]}")
    assert nums[:idx] == nums[:ans], f"Calculated array without adjacent duplicates: {nums[:idx]} doesn't match"\
                       f"Actual array without adjacent duplicates: {nums[:ans]}"

if __name__ == "__main__":
    main()
