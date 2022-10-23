# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    @classmethod
    def containsNearbyDuplicate(cls, nums: List[int], k: int) -> bool:
        num_idx_dict = {}
        for i, num in enumerate(nums):
            if num in num_idx_dict:
                if abs(num_idx_dict[num] - i ) <= k:
                    return True
                else:
                    num_idx_dict[num] = max(num_idx_dict[num], i)
            else:
                num_idx_dict[num] = i
        return False

def main():
    print("*"*25, "Example: 1", "*"*25)
    nums = [1, 2, 3, 1]
    k = 3
    print(f"Nums: {nums}, k: {k}")
    dup = Solution.containsNearbyDuplicate(nums, k)
    ans = True
    print(f"Calculated if array contains duplicate at distance less than {k}: {dup}")
    print(f"Actual if array contains duplicate at distance less than {k}: {ans}")
    assert dup == ans, f"Calculated if array contains duplicate at distance less than {k}: {dup} "\
        + f"doesn't match with Actual if array contains duplicate at distance less than {k}: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    nums = [1, 0, 1, 1]
    k = 1
    print(f"Nums: {nums}, k: {k}")
    dup = Solution.containsNearbyDuplicate(nums, k)
    ans = True
    print(f"Calculated if array contains duplicate at distance less than {k}: {dup}")
    print(f"Actual if array contains duplicate at distance less than {k}: {ans}")
    assert dup == ans, f"Calculated if array contains duplicate at distance less than {k}: {dup} "\
        + f"doesn't match with Actual if array contains duplicate at distance less than {k}: {ans}"

    print("*"*25, "Example: 3", "*"*25)
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(f"Nums: {nums}, k: {k}")
    dup = Solution.containsNearbyDuplicate(nums, k)
    ans = False
    print(f"Calculated if array contains duplicate at distance less than {k}: {dup}")
    print(f"Actual if array contains duplicate at distance less than {k}: {ans}")
    assert dup == ans, f"Calculated if array contains duplicate at distance less than {k}: {dup} "\
        + f"doesn't match with Actual if array contains duplicate at distance less than {k}: {ans}"

if __name__ == "__main__":
    main()
