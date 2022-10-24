# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List

class Solution:
    @classmethod
    def maxLength(cls, arr: List[str]) -> int:
        # First create set of alphabets from each string
        # and filter out strings with repeatable characters
        # This will give us array containing set of unique 
        # characters per string.
        nr_strings = []
        for st in arr:
            u = set(st)
            if len(u) == len(st):
                nr_strings.append(u)

        # Now we initialise the list of set.
        # and we iterate through the list of set of alphabets
        # generated above and list of set initialized now
        # and add union of the sets if both sets
        # have nothing in common ( AND is 0)
        # Finally we return max of lengths of sets.
        ans = [set()]
        for st in nr_strings:
            for a in ans:
                if not a & st:
                    ans.append(st.union(a))

        return max(len(k) for k in ans)

def main():
    print("*"*25, "Example: 1", "*"*25)
    arr = ["un", "iq", "ue"]
    print(f"Strings: {arr}")
    length = Solution.maxLength(arr)
    ans = 4
    print(f"Calculated max length of string without duplicate characters: {length}")
    print(f"Actual max length of string without duplicate characters: {ans}")
    assert length == ans, f"Calculated max length of string without duplicate characters: {length} "\
        + f"doesn't match with Actual max length of string without duplicate characters: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    arr = ["cha", "r", "act", "ers"]
    print(f"Strings: {arr}")
    length = Solution.maxLength(arr)
    ans = 6
    print(f"Calculated max length of string without duplicate characters: {length}")
    print(f"Actual max length of string without duplicate characters: {ans}")
    assert length == ans, f"Calculated max length of string without duplicate characters: {length} "\
        + f"doesn't match with Actual max length of string without duplicate characters: {ans}"

    print("*"*25, "Example: 3", "*"*25)
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    print(f"Strings: {arr}")
    length = Solution.maxLength(arr)
    ans = 26
    print(f"Calculated max length of string without duplicate characters: {length}")
    print(f"Actual max length of string without duplicate characters: {ans}")
    assert length == ans, f"Calculated max length of string without duplicate characters: {length} "\
        + f"doesn't match with Actual max length of string without duplicate characters: {ans}"

if __name__ == "__main__":
    main()
