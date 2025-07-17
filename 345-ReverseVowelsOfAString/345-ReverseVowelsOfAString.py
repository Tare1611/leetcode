# Last updated: 7/17/2025, 3:34:09 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Brute Force Approach - Use a string of vowels to check and store vowels in list and then update the string by using pop.
        # TC - O(n) SC - O(n)
        # vowels = "aeiouAEIOU"
        # vowels_list = []

        # for ch in s:
        #     if ch in vowels:
        #         vowels_list.append(ch)
        
        # reverse = ""
        # for ch in s:
        #     if ch in vowels:
        #         reverse = reverse + vowels_list.pop()
        #     else:
        #         reverse = reverse + ch
        # return reverse

        # Optimal Approach - Use 2 pointers and swap the vowels in place
        # TC - O(n) SC - O(n)
        
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

