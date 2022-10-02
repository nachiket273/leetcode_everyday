# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def __init__(self):
        self.rolls = dict()
        self.modulo = 1e9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            if target >= 1 and target <= k:
                return 1
            else:
                return 0

        if (target, n) in self.rolls:
            return self.rolls[(target, n)]
        else:
            self.rolls[(target, n)] = 0
            for i in range(1, k+1):
                self.rolls[(target, n)] += self.numRollsToTarget(n-1, k, target-i)
            self.rolls[(target, n)] %= self.modulo
            return int(self.rolls[(target, n)])

def main():
    print("*"*25, "Example: 1", "*"*25)
    n = 1
    k = 6
    target = 3
    print(f"Number of dices: {n}, faces per dice: {k}, target: {target}")
    num_rolls = Solution().numRollsToTarget(n, k, target)
    ans = 1
    print(f"Expected Number of Rolls: {ans}")
    print(f"Calculated Number of Rolls: {num_rolls}")
    assert ans == num_rolls, f"Calculated Number of Rolls {num_rolls} doesn't"\
        + f" match with Expected Number of Rolls {ans}"

    print("*"*25, "Example: 2", "*"*25)
    n = 2
    k = 6
    target = 7
    print(f"Number of dices: {n}, faces per dice: {k}, target: {target}")
    num_rolls = Solution().numRollsToTarget(n, k, target)
    ans = 6
    print(f"Expected Number of Rolls: {ans}")
    print(f"Calculated Number of Rolls: {num_rolls}")
    assert ans == num_rolls, f"Calculated Number of Rolls {num_rolls} doesn't"\
        + f" match with Expected Number of Rolls {ans}"

    print("*"*25, "Example: 3", "*"*25)
    n = 30
    k = 30
    target = 500
    print(f"Number of dices: {n}, faces per dice: {k}, target: {target}")
    num_rolls = Solution().numRollsToTarget(n, k, target)
    ans = 222616187
    print(f"Expected Number of Rolls: {ans}")
    print(f"Calculated Number of Rolls: {num_rolls}")
    assert ans == num_rolls, f"Calculated Number of Rolls {num_rolls} doesn't"\
        + f" match with Expected Number of Rolls {ans}"

if __name__ == "__main__":
    main()
