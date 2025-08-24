# Last updated: 8/24/2025, 12:07:54 PM
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Approach - Use the join condition and check if the strings are equla or not

        w1 = "".join(word1)
        w2 = "".join(word2)

        return w1==w2