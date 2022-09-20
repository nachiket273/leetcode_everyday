# https://leetcode.com/problems/palindrome-pairs/

from typing import List

class Solution:
    def __init__(self):
        self.word_dict = {}

    def ispalindrome(self, string: str) -> bool:
        return string == string[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []

        for i, word in enumerate(words):
            self.word_dict[word[::-1]] = i

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]

                if prefix in self.word_dict.keys() and self.ispalindrome(suffix)\
                    and self.word_dict[prefix] != i:
                    ans.append([i, self.word_dict[prefix]])
                if len(prefix) and suffix in self.word_dict.keys()\
                    and self.ispalindrome(prefix) and self.word_dict[suffix] != i:
                    ans.append([self.word_dict[suffix], i])

        return ans

def main():
    print("*"*25, "Example: 1", "*"*25)
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(f"Words: {words}")
    sol = Solution()
    pal = sol.palindromePairs(words)
    ans = [[0,1], [1,0], [3,2], [2,4]]
    print(f"Expected Palidrome Pairs: {ans}")
    print(f"Calculated Palidrome Pairs: {pal}")
    assert set(map(tuple, ans)) == set(map(tuple, pal)),\
        f"Calculated Palidrome Pairs {pal} doesn't"\
            + f" match with Expected Palidrome Pairs {ans}"
    print("Palindromes:")
    print(" ".join([words[pair[0]] + words[pair[1]] for pair in pal]))

    print("*"*25, "Example: 2", "*"*25)
    words = ["bat", "tab", "cat"]
    print(f"Words: {words}")
    sol = Solution()
    pal = sol.palindromePairs(words)
    ans = [[0,1], [1,0]]
    print(f"Expected Palidrome Pairs: {ans}")
    print(f"Calculated Palidrome Pairs: {pal}")
    assert set(map(tuple, ans)) == set(map(tuple, pal)),\
        f"Calculated Palidrome Pairs {pal} doesn't"\
            + f" match with Expected Palidrome Pairs {ans}"
    print("Palindromes:")
    print(" ".join([words[pair[0]] + words[pair[1]] for pair in pal]))

if __name__ == "__main__":
    main()
