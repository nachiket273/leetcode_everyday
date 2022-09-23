# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    @classmethod
    def concatenatedBinary(cls, n: int) -> int:
        ans = 0
        mod = 10**9 + 7
        for i in range(1, n+1):
            if i == 1:
                ans = i
            else:
                num_bits = i.bit_length()
                ans = (ans << num_bits) % mod
                ans = (ans + i ) % mod

        return int(ans)

def main():
    print("*"*25, "Example: 1", "*"*25)
    n = 1
    print(f"Number: {n}")
    num = Solution.concatenatedBinary(n)
    ans = 1
    print(f"Expected Decimal No: {ans}")
    print(f"Calculated Decimal No: {num}")
    assert ans == num, f"Calculated Decimal No {num} doesn't"\
        + f" match with Expected Decimal No {ans}"

    print("*"*25, "Example: 2", "*"*25)
    n = 3
    print(f"Number: {n}")
    num = Solution.concatenatedBinary(n)
    ans = 27
    print(f"Expected Decimal No: {ans}")
    print(f"Calculated Decimal No: {num}")
    assert ans == num, f"Calculated Decimal No {num} doesn't"\
        + f" match with Expected Decimal No {ans}"

    print("*"*25, "Example: 3", "*"*25)
    n = 12
    print(f"Number: {n}")
    num = Solution.concatenatedBinary(n)
    ans = 505379714
    print(f"Expected Decimal No: {ans}")
    print(f"Calculated Decimal No: {num}")
    assert ans == num, f"Calculated Decimal No {num} doesn't"\
        + f" match with Expected Decimal No {ans}"

if __name__ == "__main__":
    main()