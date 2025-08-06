# Last updated: 8/6/2025, 3:03:16 PM
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        

        position.sort()
        
        def placeBalls(minDist):
            count = 1
            lastPos = position[0]

            for i in range(1, len(position)):
                if position[i] - lastPos >= minDist:
                    count += 1
                    lastPos = position[i]
                if count >= m:
                    return True
            return False
        
        low = 1
        high = position[-1] - position[0]

        result = 0

        while low <= high:
            mid = (low + high) // 2
            if placeBalls(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result