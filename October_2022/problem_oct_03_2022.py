# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import List

class Solution:
    @classmethod
    def minCost(cls, colors: str, neededTime: List[int]) -> int:
        cost = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                if neededTime[i] < neededTime[i+1]:
                    cost += neededTime[i]
                else:
                    cost += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
        return cost

def main():
    print("*"*25, "Example: 1", "*"*25)
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    print(f"Colors: {colors}, Time needed per removal: {neededTime}")
    cost = Solution.minCost(colors, neededTime)
    ans = 3
    print(f"Expected Min Cost: {ans}")
    print(f"Calculated Min Cost: {cost}")
    assert ans == cost, f"Calculated Min Cost {cost} doesn't"\
        + f" match with Expected Min Cost {ans}"

    print("*"*25, "Example: 2", "*"*25)
    colors = "abc"
    neededTime = [1, 2, 3]
    print(f"Colors: {colors}, Time needed per removal: {neededTime}")
    cost = Solution.minCost(colors, neededTime)
    ans = 0
    print(f"Expected Min Cost: {ans}")
    print(f"Calculated Min Cost: {cost}")
    assert ans == cost, f"Calculated Min Cost {cost} doesn't"\
        + f" match with Expected Min Cost {ans}"

    print("*"*25, "Example: 3", "*"*25)
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print(f"Colors: {colors}, Time needed per removal: {neededTime}")
    cost = Solution.minCost(colors, neededTime)
    ans = 2
    print(f"Expected Min Cost: {ans}")
    print(f"Calculated Min Cost: {cost}")
    assert ans == cost, f"Calculated Min Cost {cost} doesn't"\
        + f" match with Expected Min Cost {ans}"

if __name__ == "__main__":
    main()