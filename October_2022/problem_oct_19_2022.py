# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
from typing import List

class Solution:
    @classmethod
    def topKFrequent(cls, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        ans = sorted(cntr, key=lambda x: (-cntr[x], x))
        return ans[:k]

def main():
    print("*"*25, "Example: 1", "*"*25)
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(f"All words: {words}\tk: {k}")
    kwords = Solution.topKFrequent(words, k)
    ans = ["i", "love"]
    print(f"Calculated {k} frequent words: {kwords}")
    print(f"Actual {k} frequent words: {ans}")
    assert kwords == ans, f"Calculated {k} frequent words: {kwords} "\
        + f"doesn't match with Actual {k} frequent words: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    words = ["the", "day", "is", "sunny", "the",
             "the", "the", "sunny", "is", "is"]
    k = 4
    print(f"All words: {words}\tk: {k}")
    kwords = Solution.topKFrequent(words, k)
    ans = ["the","is","sunny","day"]
    print(f"Calculated {k} frequent words: {kwords}")
    print(f"Actual {k} frequent words: {ans}")
    assert kwords == ans, f"Calculated {k} frequent words: {kwords} "\
        + f"doesn't match with Actual {k} frequent words: {ans}"

if __name__ == "__main__":
    main()
