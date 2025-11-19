# Last updated: 11/19/2025, 1:00:07 AM
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Approach - Base idea is to traverse through the length of the input string and check if the index is equal to
        # - the value in the spaces array and then update the resultant array
        result = []
        p = 0
        if len(spaces) == 0:
            return s
        for i in range(len(s)):
            if p < len(spaces) and i == spaces[p]:
                result.append(' ')
                # result.append(s[i])
                p += 1
            result.append(s[i])
        return ''.join(result)