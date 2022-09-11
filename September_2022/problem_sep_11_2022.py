# https://leetcode.com/problems/maximum-performance-of-a-team/

import heapq
from typing import List


class Solution:
    @classmethod
    def maxPerformance(cls, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MODULO = 10 ** 9 + 7
        candidates = sorted(zip(efficiency, speed), reverse=True)
        res, ssum = 0, 0
        heap = []
        for (eff, sp) in candidates:
            heapq.heappush(heap, sp)
            ssum += sp
            if len(heap) > k :
                ssum -= heapq.heappop(heap)
            res = max(res, ssum * eff)

        return res % MODULO

def main():
    print("*"*25, "Example: 1", "*"*25)
    n, speed, efficiency, k = 6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2
    print(f"number of candidates: {n}, speed: {speed}, efficiency: {efficiency}, k: {k}")
    max_perf = Solution.maxPerformance(n, speed, efficiency, k)
    ans = 60
    print(f"Expected Max Peformance: {ans}")
    print(f"Calculated Max Peformance: {max_perf}")
    assert ans == max_perf, f"Calculated Max Peformance {max_perf} doesn't"\
                            + " match with Expected Max Peformance {ans}"

    print("*"*25, "Example: 1", "*"*25)
    n, speed, efficiency, k = 6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3
    print(f"number of candidates: {n}, speed: {speed}, efficiency: {efficiency}, k: {k}")
    max_perf = Solution.maxPerformance(n, speed, efficiency, k)
    ans = 68
    print(f"Expected Max Peformance: {ans}")
    print(f"Calculated Max Peformance: {max_perf}")
    assert ans == max_perf, f"Calculated Max Peformance {max_perf} doesn't"\
                            + " match with Expected Max Peformance {ans}"

    print("*"*25, "Example: 1", "*"*25)
    n, speed, efficiency, k = 6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4
    print(f"number of candidates: {n}, speed: {speed}, efficiency: {efficiency}, k: {k}")
    max_perf = Solution.maxPerformance(n, speed, efficiency, k)
    ans = 72
    print(f"Expected Max Peformance: {ans}")
    print(f"Calculated Max Peformance: {max_perf}")
    assert ans == max_perf, f"Calculated Max Peformance {max_perf} doesn't"\
                            + " match with Expected Max Peformance {ans}"

if __name__ == "__main__":
    main()
