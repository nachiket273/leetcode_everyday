# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

from typing import List

class Solution:
    @classmethod
    def sumEvenAfterQueries(cls, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_sum = sum([k for k in nums if k%2==0])

        for (val, idx) in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            ans.append(even_sum)

        return ans

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(f"Nums: {nums}, Queries: {queries}")
    even_sum = Solution.sumEvenAfterQueries(nums, queries)
    ans = [8, 6, 2, 4]
    print(f"Expected Even Sum: {ans}")
    print(f"Calculated Even Sum: {even_sum}")
    assert ans == even_sum, f"Calculated Even Sum {even_sum} doesn't"\
        + f" match with Expected Even Sum {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [1]
    queries = [[4,0]]
    print(f"Nums: {nums}, Queries: {queries}")
    even_sum = Solution.sumEvenAfterQueries(nums, queries)
    ans = [0]
    print(f"Expected Even Sum: {ans}")
    print(f"Calculated Even Sum: {even_sum}")
    assert ans == even_sum, f"Calculated Even Sum {even_sum} doesn't"\
        + f" match with Expected Even Sum {ans}"

if __name__ == "__main__":
    main()
