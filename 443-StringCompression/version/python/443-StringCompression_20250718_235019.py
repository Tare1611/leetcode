# Last updated: 7/18/2025, 11:50:19 PM
# Optimal Approach to the question reducing the SC to O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []
        sumaltitude = 0

        for i in range(len(gain)): 
            sumaltitude += gain[i]
            altitude.append(sumaltitude)

        highest = 0
        for i in range(len(altitude)): 
            if highest < altitude[i]: 
                highest = altitude[i]

        return highest