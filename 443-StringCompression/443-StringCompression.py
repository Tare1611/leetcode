# Last updated: 7/17/2025, 8:39:25 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        # Approach - Use for loop to traverse through
        # TC - O(n) SC - O(1)
        result = []
        n = len(chars)
        num = 1

        if n <= 1:
            return n

        for i in range(1, n):
            if chars[i - 1] == chars[i]:
                num += 1
            else:
                result.append(chars[i - 1])
                if num > 1:
                    result.extend(list(str(num)))
                num = 1

        result.append(chars[-1])
        if num > 1:
            result.extend(list(str(num)))

        chars[:] = result
        return len(chars)