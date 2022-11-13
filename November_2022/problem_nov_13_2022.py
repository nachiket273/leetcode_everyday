# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    @classmethod
    def reverseWords(cls, s: str) -> str:
        return " ".join(s.split()[::-1])

def main():
    print("*"*25, "Example: 1", "*"*25)
    s = "the sky is blue"
    print(f"String: {s}")
    str1 = Solution.reverseWords(s)
    ans = "blue is sky the"
    print(f"Calculated string with words in reverse order: {str1}")
    print(f"Actual string with words in reverse order: {ans}")
    assert ans == str1, f"Calculated string with words in reverse order: {str1} doesn't match"\
                       f"Actual string with words in reverse order: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    s = "  hello world  "
    print(f"String: {s}")
    str1 = Solution.reverseWords(s)
    ans = "world hello"
    print(f"Calculated string with words in reverse order: {str1}")
    print(f"Actual string with words in reverse order: {ans}")
    assert ans == str1, f"Calculated string with words in reverse order: {str1} doesn't match"\
                       f"Actual string with words in reverse order: {ans}"

if __name__ == "__main__":
    main()