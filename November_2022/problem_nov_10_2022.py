# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    @classmethod
    def removeDuplicates(cls, s: str) -> str:
        res = ""
        for char in s:
            if len(res) > 0 and res[-1] == char:
                res = res[:-1]
            else:
                res += char

        return res

def main():
    print("*"*25, "Example: 1", "*"*25)
    s = "abbaca"
    print(f"string: {s}")
    out = Solution.removeDuplicates(s)
    ans = "ca"
    print(f"Calculated string without adjacent duplicates: {out}")
    print(f"Actual string without adjacent duplicates: {ans}")
    assert ans == out, f"Calculated string without adjacent duplicates: {out} doesn't match"\
                       f"Actual string without adjacent duplicates: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    s = "azxxzy"
    print(f"string: {s}")
    out = Solution.removeDuplicates(s)
    ans = "ay"
    print(f"Calculated string without adjacent duplicates: {out}")
    print(f"Actual string without adjacent duplicates: {ans}")
    assert ans == out, f"Calculated string without adjacent duplicates: {out} doesn't match"\
                       f"Actual string without adjacent duplicates: {ans}"

if __name__ == "__main__":
    main()
