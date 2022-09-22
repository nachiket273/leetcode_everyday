# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

from typing import List

class Solution:
    @classmethod
    def maximumScore(cls, nums: List[int], multipliers: List[int]) -> int:
        mult_len, nums_len = len(multipliers), len(nums)
        dp = [[0 for _ in range(mult_len+1)] for _ in range(mult_len+1)]

        for op in range(mult_len-1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op+1][left+1],
                    multipliers[op] * nums[nums_len-1-(op-left)] + dp[op+1][left]
                )

        return dp[0][0]

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    print(f"Nums: {nums}, Multipliers: {multipliers}")
    score = Solution.maximumScore(nums, multipliers)
    ans = 14
    print(f"Expected Maximum Score: {ans}")
    print(f"Calculated Maximum Score: {score}")
    assert ans == score, f"Calculated Maximum Score {score} doesn't"\
            + f" match with Expected Maximum Score {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    print(f"Nums: {nums}, Multipliers: {multipliers}")
    score = Solution.maximumScore(nums, multipliers)
    ans = 102
    print(f"Expected Maximum Score: {ans}")
    print(f"Calculated Maximum Score: {score}")
    assert ans == score, f"Calculated Maximum Score {score} doesn't"\
            + f" match with Expected Maximum Score {ans}"

if __name__ == "__main__":
    main()
