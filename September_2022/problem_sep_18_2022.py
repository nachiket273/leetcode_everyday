# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    @classmethod
    def trap(cls, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1

        return ans

def main():
    print("*"*25, "Example: 1", "*"*25)
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Heights {height}")
    units = Solution.trap(height)
    ans = 6
    print(f"Expected Trapped Water: {ans}")
    print(f"Calculated Trapped Water: {units}")
    assert ans == units, f"Calculated duplicates {units} doesn't"\
            + f" match with Expected duplicates {ans}"

    print("*"*25, "Example: 2", "*"*25)
    height = [4, 2, 0, 3, 2, 5]
    print(f"Heights {height}")
    units = Solution.trap(height)
    ans = 9
    print(f"Expected Trapped Water: {ans}")
    print(f"Calculated Trapped Water: {units}")
    assert ans == units, f"Calculated duplicates {units} doesn't"\
            + f" match with Expected duplicates {ans}"

if __name__ == "__main__":
    main()
