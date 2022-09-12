# https://leetcode.com/problems/bag-of-tokens/

from collections import deque
from typing import List


class Solution:
    @classmethod
    def bagOfTokensScore(cls, tokens: List[int], power: int) -> int:
        tokens.sort()
        queue = deque(tokens)
        ret, score = 0, 0
        while queue and (power >= queue[0] or score > 0):
            while queue and power >= queue[0]:
                power -= queue.popleft()
                score += 1
            ret = max(ret, score)

            if queue and score:
                power += queue.pop()
                score -= 1

        return ret

def main():
    print("*"*25, "Example: 1", "*"*25)
    tokens, power = [100], 50
    print(f"tokens: {tokens}, power: {power}")
    score = Solution.bagOfTokensScore(tokens, power)
    ans = 0
    print(f"Expected Score: {ans}")
    print(f"Calculated Score: {score}")
    assert ans == score, f"Calculated Score {score} doesn't"\
                            + f" match with Expected Score {ans}"

    print("*"*25, "Example: 2", "*"*25)
    tokens, power = [100, 200], 150
    print(f"tokens: {tokens}, power: {power}")
    score = Solution.bagOfTokensScore(tokens, power)
    ans = 1
    print(f"Expected Score: {ans}")
    print(f"Calculated Score: {score}")
    assert ans == score, f"Calculated Score {score} doesn't"\
                            + f" match with Expected Score {ans}"

    print("*"*25, "Example: 3", "*"*25)
    tokens, power = [100, 200, 300, 400], 200
    print(f"tokens: {tokens}, power: {power}")
    score = Solution.bagOfTokensScore(tokens, power)
    ans = 2
    print(f"Expected Score: {ans}")
    print(f"Calculated Score: {score}")
    assert ans == score, f"Calculated Score {score} doesn't"\
                            + f" match with Expected Score {ans}"

if __name__ == "__main__":
    main()
