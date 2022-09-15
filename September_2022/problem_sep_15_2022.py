# https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter
from typing import List

class Solution:
    @classmethod
    def findOriginalArray(cls, changed: List[int]) -> List[int]:
        res = []

        if len(changed) % 2:
            return res

        changed = sorted(changed)
        changed_counter = Counter(changed)

        for num in changed:
            if changed_counter[num] == 0:
                continue
            if changed_counter.get(2 * num, 0) >= 1:
                res.append(num)
                changed_counter[2 * num] -= 1
                changed_counter[num] -= 1

            else:
                return []

        return res

def main():
    print("*"*25, "Example: 1", "*"*25)
    changed = [1, 3, 4, 2, 6, 8]
    print(f"Changed array: {changed}")
    orig = Solution.findOriginalArray(changed)
    ans = [1, 3, 4]
    print(f"Original Array: {ans}")
    print(f"Calculated Array: {orig}")
    assert ans == orig, f"Calculated Array {orig} doesn't"\
                            + f" match with Actual Array {ans}"

    print("*"*25, "Example: 2", "*"*25)
    changed = [6, 3, 0, 1]
    print(f"Changed array: {changed}")
    orig = Solution.findOriginalArray(changed)
    ans = []
    print(f"Original Array: {ans}")
    print(f"Calculated Array: {orig}")
    assert ans == orig, f"Calculated Array {orig} doesn't"\
                            + f" match with Actual Array {ans}"

    print("*"*25, "Example: 3", "*"*25)
    changed = [1]
    print(f"Changed array: {changed}")
    orig = Solution.findOriginalArray(changed)
    ans = []
    print(f"Original Array: {ans}")
    print(f"Calculated Array: {orig}")
    assert ans == orig, f"Calculated Array {orig} doesn't"\
                            + f" match with Actual Array {ans}"

if __name__ == "__main__":
    main()
