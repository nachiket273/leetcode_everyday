# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    @classmethod
    def checkIfPangram(cls, sentence: str) -> bool:
        seen = 0
        for char in sentence:
            ascii_char = ord(char) - ord('a')
            bit_repr = 1 << ascii_char
            seen |= bit_repr

        return seen == (1 << 26) - 1

def main():
    print("*"*25, "Example: 1", "*"*25)
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(f"Sentence: {sentence}")
    is_pangram = Solution.checkIfPangram(sentence)
    ans = True
    print(f"Calculated if sentence pangram: {is_pangram}")
    print(f"Sentence actually pangram: {ans}")
    assert is_pangram == ans, f"Calculated if sentence pangram: {is_pangram} "\
        + f"doesn't match with Sentence actually pangram: {ans}"

    print("*"*25, "Example: 2", "*"*25)
    sentence = "leetcode"
    print(f"Sentence: {sentence}")
    is_pangram = Solution.checkIfPangram(sentence)
    ans = False
    print(f"Calculated if sentence pangram: {is_pangram}")
    print(f"Sentence actually pangram: {ans}")
    assert is_pangram == ans, f"Calculated if sentence pangram: {is_pangram} "\
        + f"doesn't match with Sentence actually pangram: {ans}"

if __name__ == "__main__":
    main()
