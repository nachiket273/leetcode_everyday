# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List


class Solution:
    def __init__(self):
        self.ret = []
        
    def dfs(self, n: int, k: int, num: int) -> None:
        if n == 0:
            self.ret.append(num)
        else:
            last_dig = num % 10
            next_possible_digs = set([last_dig+k, last_dig-k])
        
            for dig in next_possible_digs:
                if 0 <= dig < 10:
                    new_num = num * 10 + dig
                    self.dfs(n-1, k, new_num)

    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(1, 10)]
        
        for num in range(1, 10):
            self.dfs(n-1, k, num)
            
        return self.ret

def main():
    print("*"*25, "Example: 1", "*"*25)
    n, k = 3, 7
    print(f"n: {n}, k: {k}")
    sol = Solution()
    nums = sol.numsSameConsecDiff(n, k)
    ans = [181, 292, 707, 818, 929]
    print(f"Expected Numbers: {ans}")
    print(f"Returned Numbers: {nums}")
    assert set(ans) == set(nums), f"Output {nums} doesn't match with answer {ans}"

    print("*"*25, "Example: 2", "*"*25)
    n1, k1 = 2, 1
    print(f"n: {n1}, k: {k1}")
    sol1 = Solution()
    nums1 = sol1.numsSameConsecDiff(n1, k1)
    ans1 = [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    print(f"Expected Numbers: {ans1}")
    print(f"Returned Numbers: {nums1}")
    assert set(ans1) == set(nums1), f"Output {nums1} doesn't match with answer {ans1}"

if __name__ == "__main__":
    main()
