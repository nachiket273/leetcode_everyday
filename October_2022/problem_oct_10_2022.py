# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    @classmethod
    def breakPalindrome(cls, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        change_idx = 0
        while change_idx < n//2 and palindrome[change_idx] == 'a':
            change_idx += 1

        if change_idx == n//2:
            return palindrome[:n-1]  + 'b'

        return palindrome[:change_idx] + 'a' + palindrome[change_idx+1:]

def main():
    print("*"*25, "Example: 1", "*"*25)
    palindrome = "abccba"
    print(f"Palindrome: {palindrome}")
    res = Solution.breakPalindrome(palindrome)
    ans = "aaccba"
    print(f"Expected Closest Non-Palindrome: {ans}")
    print(f"Calculated Closest Non-Palindrome: {res}")
    assert ans == res, f"Calculated Closest Non-Palindrome {res} "\
        + f"doesn't match with Expected Closest Non-Palindrome {ans}"

    print("*"*25, "Example: 2", "*"*25)
    palindrome = "a"
    print(f"Palindrome: {palindrome}")
    res = Solution.breakPalindrome(palindrome)
    ans = ""
    print(f"Expected Closest Non-Palindrome: {ans}")
    print(f"Calculated Closest Non-Palindrome: {res}")
    assert ans == res, f"Calculated Closest Non-Palindrome {res} "\
        + f"doesn't match with Expected Closest Non-Palindrome {ans}"

if __name__ == "__main__":
    main()
