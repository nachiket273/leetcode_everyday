# https://leetcode.com/problems/integer-to-roman/

class Solution:
    @classmethod
    def intToRoman(cls, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans = ''
        i = 0
        while num:
            while num >= nums[i]:
                ans += symbs[i]
                num -= nums[i]
            i += 1

        return ans

def main():
    print("*"*25, "Example: 1", "*"*25)
    num = 3
    print(f"Number in decimal system: {num}")
    roman = Solution.intToRoman(num)
    ans = "III"
    print(f"Calculated roman representation: {roman}")
    print(f"Actual roman representation: {ans}")
    assert roman == ans, f"Calculated roman representation: {roman} "\
        + f"doesn't match with Actual roman representation: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    num = 58
    print(f"Number in decimal system: {num}")
    roman = Solution.intToRoman(num)
    ans = "LVIII"
    print(f"Calculated roman representation: {roman}")
    print(f"Actual roman representation: {ans}")
    assert roman == ans, f"Calculated roman representation: {roman} "\
        + f"doesn't match with Actual roman representation: {ans}"

    print("*"*25, "Example: 3", "*"*25)
    num = 1994
    print(f"Number in decimal system: {num}")
    roman = Solution.intToRoman(num)
    ans = "MCMXCIV"
    print(f"Calculated roman representation: {roman}")
    print(f"Actual roman representation: {ans}")
    assert roman == ans, f"Calculated roman representation: {roman} "\
        + f"doesn't match with Actual roman representation: {ans}"

if __name__ == "__main__":
    main()
