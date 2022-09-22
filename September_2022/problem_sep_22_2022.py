# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    @classmethod
    def reverseWords(cls, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())

def main():
    print("*"*25, "Example: 1", "*"*25)
    s = "Let's take LeetCode contest"
    print(f"String: {s}")
    rev_str = Solution.reverseWords(s)
    ans = "s'teL ekat edoCteeL tsetnoc"
    print(f"Expected Reverse String: {ans}")
    print(f"Calculated Reverse String: {rev_str}")
    assert ans == rev_str, f"Calculated Reverse String {rev_str} doesn't"\
        + f" match with Expected Reverse String {ans}"

    print("*"*25, "Example: 2", "*"*25)
    s = "God Ding"
    print(f"String: {s}")
    rev_str = Solution.reverseWords(s)
    ans = "doG gniD"
    print(f"Expected Reverse String: {ans}")
    print(f"Calculated Reverse String: {rev_str}")
    assert ans == rev_str, f"Calculated Reverse String {rev_str} doesn't"\
        + f" match with Expected Reverse String {ans}"

if __name__ == "__main__":
    main()
