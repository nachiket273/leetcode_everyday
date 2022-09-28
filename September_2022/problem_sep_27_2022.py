# https://leetcode.com/problems/push-dominoes/

class Solution:
    @classmethod
    def pushDominoes(cls, dominoes: str) -> str:
        n = len(dominoes)
        rnk = [0 for _ in range(n)]
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f= max(f-1, 0)
            rnk[i] += f            

        f = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == '.':
                f = max(f-1, 0)
            else:
                f = 0
            rnk[i] -= f

        return "".join(['.' if k == 0 else 'L' if k < 0 else 'R' for k in rnk])

def main():
    print("*"*25, "Example: 1", "*"*25)
    dominoes = "RR.L"
    print(f"Intial Domino Positions: {dominoes}")
    final_pos = Solution.pushDominoes(dominoes)
    ans = "RR.L"
    print(f"Calculated Dominoes Position: {final_pos}")
    print(f"Expected Dominoes Position: {ans}")
    assert ans == final_pos, f"Calculated Dominoes Position {final_pos} doesn't"\
        + f" match with Expected Dominoes Position {ans}"

    print("*"*25, "Example: 2", "*"*25)
    dominoes = ".L.R...LR..L.."
    print(f"Intial Domino Positions: {dominoes}")
    final_pos = Solution.pushDominoes(dominoes)
    ans = "LL.RR.LLRRLL.."
    print(f"Calculated Dominoes Position: {final_pos}")
    print(f"Expected Dominoes Position: {ans}")
    assert ans == final_pos, f"Calculated Dominoes Position {final_pos} doesn't"\
        + f" match with Expected Dominoes Position {ans}"

if __name__ == "__main__":
    main()

