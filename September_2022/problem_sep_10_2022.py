# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
from typing import List


class Solution:
    @classmethod
    def maxProfit(cls, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            max_bal = -prices[0]
            dp[i][0] = 0
            for j in range(1, len(prices)):
                max_bal = max(max_bal, dp[i-1][j-1] - prices[j])
                dp[i][j] = max(max_bal + prices[j], dp[i][j-1])
                
        return dp[k][len(prices)-1]

def main():
    print("*"*25, "Example: 1", "*"*25)
    k, prices = 2, [2,4,1]
    print(f"k: {k}, prices: {prices}")
    profit = Solution.maxProfit(k, prices)
    ans = 2
    print(f"Expected Max Profit: {ans}")
    print(f"Calculated Max Profit: {profit}")
    assert ans == profit, f"Calculated Max Profit {profit} doesn't"\
                          + f" match with Expected Max Profit {ans}"

    print("*"*25, "Example: 2", "*"*25)
    k, prices = 2, [3, 2, 6, 5, 0, 3]
    print(f"k: {k}, prices: {prices}")
    profit = Solution.maxProfit(k, prices)
    ans = 7
    print(f"Expected Max Profit: {ans}")
    print(f"Calculated Max Profit: {profit}")
    assert ans == profit, f"Calculated Max Profit {profit} doesn't"\
                          + f" match with Expected Max Profit {ans}"

if __name__ == "__main__":
    main()
