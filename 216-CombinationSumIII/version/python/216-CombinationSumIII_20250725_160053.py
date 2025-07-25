# Last updated: 7/25/2025, 4:00:53 PM
# 2-D array for keeping a track
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Approach 2-D array with chars of word 1 and word 2, go with bottom up approach and also have additional row and col at end to store the length of words till the cell
        # TC - O(m*n) SC - O(m*n) where m & n are lengths of word1 and word2

        cache = [[float("inf")]*(len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]