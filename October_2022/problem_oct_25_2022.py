# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import List

class Solution:
    @classmethod
    def arrayStringsAreEqual(cls, word1: List[str], word2: List[str]) :
        str1 = "".join(word1)
        str2 = "".join(word2)
        return str1 == str2, str1, str2

def main():
    print("*"*25, "Example: 1", "*"*25)
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(f"Word1: {word1}, Word2: {word2}")
    same, str1, str2 = Solution.arrayStringsAreEqual(word1, word2)
    ans = True
    print(f"String from array1 : {str1}")
    print(f"String from array2 : {str2}")
    print(f"Are both strings same: {ans}")
    print(f"Calculated : {same}")

    print("*"*25, "Example: 2", "*"*25)
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(f"Word1: {word1}, Word2: {word2}")
    same, str1, str2 = Solution.arrayStringsAreEqual(word1, word2)
    ans = False
    print(f"String from array1 : {str1}")
    print(f"String from array2 : {str2}")
    print(f"Are both strings same: {ans}")
    print(f"Calculated : {same}")

    print("*"*25, "Example: 3", "*"*25)
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(f"Word1: {word1}, Word2: {word2}")
    same, str1, str2 = Solution.arrayStringsAreEqual(word1, word2)
    ans = True
    print(f"String from array1 : {str1}")
    print(f"String from array2 : {str2}")
    print(f"Are both strings same: {ans}")
    print(f"Calculated : {same}")

if __name__ == "__main__":
    main()
