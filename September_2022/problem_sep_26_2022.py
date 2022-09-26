# https://leetcode.com/problems/satisfiability-of-equality-equations/

from collections import defaultdict
from typing import List

class Solution:
    def __init__(self):
        self.parent = defaultdict(lambda: '-1')

    def find(self, val):
        if self.parent[val] == '-1':
            return val
        return self.find(self.parent[val])

    def union(self, val1, val2):
        par1 = self.find(val1)
        par2 = self.find(val2)

        if par1 != par2:
            self.parent[par1] = par2

    def equationsPossible(self, equations: List[str]) -> bool:
        for eq in equations:
            if eq[1] == '=':
                self.union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == '!':
                if self.find(eq[0]) == self.find(eq[3]):
                    return False

        return True

def main():
    print("*"*25, "Example: 1", "*"*25)
    equations = ["a==b","b!=a"]
    print(f"Equations: {equations}")
    is_possible = Solution().equationsPossible(equations)
    ans = False
    print(f"Are Equations Possible: {ans}")
    print(f"Calculated if Equations Possible: {is_possible}")
    assert ans == is_possible, f"Calculated if Equations Possible {is_possible} doesn't"\
        + f" match with Answer if Equations Possible {ans}"

    print("*"*25, "Example: 2", "*"*25)
    equations = ["b==a","a==b"]
    print(f"Equations: {equations}")
    is_possible = Solution().equationsPossible(equations)
    ans = True
    print(f"Are Equations Possible: {ans}")
    print(f"Calculated if Equations Possible: {is_possible}")
    assert ans == is_possible, f"Calculated if Equations Possible {is_possible} doesn't"\
        + f" match with Answer if Equations Possible {ans}"

if __name__ == "__main__":
    main()
