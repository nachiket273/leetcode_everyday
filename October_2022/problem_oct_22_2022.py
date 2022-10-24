# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    @classmethod
    def minWindow(cls, s: str, t: str) -> str:
        if not s or not t or len(s) == 0 or len(t) == 0: 
            return ""

        tcounts = Counter(t)
        left, right = 0, 0
        tunique = len(tcounts)
        numcharst = 0
        cnts = {}
        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            cnts[char] = cnts.get(char, 0) + 1

            if char in tcounts and cnts[char] == tcounts[char]:
                numcharst += 1

            while left <= right and numcharst == tunique:
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                cnts[char] -= 1
                if char in tcounts and cnts[char] < tcounts[char]:
                    numcharst -= 1

                left += 1    

            right += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

def main():
    print("*"*25, "Example: 1", "*"*25)
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"String1: {s}, String2: {t}")
    sub = Solution.minWindow(s, t)
    ans = "BANC"
    print(f"Calculated minimum substring: {sub}")
    print(f"Actual minimum substring: {ans}")
    assert sub == ans, f"Calculated minimum substring: {sub} "\
        + f"doesn't match with Actual minimum substring: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    s = "a"
    t = "a"
    print(f"String1: {s}, String2: {t}")
    sub = Solution.minWindow(s, t)
    ans = "a"
    print(f"Calculated minimum substring: {sub}")
    print(f"Actual minimum substring: {ans}")
    assert sub == ans, f"Calculated minimum substring: {sub} "\
        + f"doesn't match with Actual minimum substring: {ans}"

    print("*"*25, "Example: 3", "*"*25)
    s = "a"
    t = "aa"
    print(f"String1: {s}, String2: {t}")
    sub = Solution.minWindow(s, t)
    ans = ""
    print(f"Calculated minimum substring: {sub}")
    print(f"Actual minimum substring: {ans}")
    assert sub == ans, f"Calculated minimum substring: {sub} "\
        + f"doesn't match with Actual minimum substring: {ans}"

if __name__ == "__main__":
    main()
