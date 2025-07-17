# Last updated: 7/17/2025, 3:34:14 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        # Brute Force Approach - without using inbuilt function apart from strip loop through the string and reverse
        # TC - O(n^2) SC - O(n)
        # words = []
        # word = ''

        # for ch in s:
        #     if ch != ' ':
        #         word += ch
        #     elif word:
        #         words.append(word)
        #         word = ''
        # if word:
        #     words.append(word)
        
        # reversedwords = ''
        # for i in range(len(words)-1, -1, -1):
        #     reversedwords += words[i] + ' '

        # return reversedwords.strip()
        
        # Optimal Approach - Use inbuilt functions 
        # TC - O(n) SC - O(n)
        words = s.strip().split()

        return ' '.join(reversed(words))