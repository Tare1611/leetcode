# Last updated: 7/29/2025, 1:44:02 PM
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
        # words = s.strip().split()

        # return ' '.join(reversed(words))

        # Approach - To reduce the SC to O(1) we can use two pointers after splitting the string
        l = 0
        s = s.strip().split()
        r = len(s) - 1
        # print(s)
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ' '.join(s)
