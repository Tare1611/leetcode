# Last updated: 7/28/2025, 11:10:57 AM
# Merge both array and start in reverse order, position closest to the target
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Approach - Copmbine the position and speed into 1 array of array, then sort the array according to start position in decreasing order
        # Calculate the time taken to reach target by the nearest car and check if the cars behind catchup if yes fleet += 1
        # TC - O(nlogn)
        # SC - O(n)

        stack = [[p, s] for p, s in zip(position, speed)]
        fleet = []
        
        for p, s in sorted(stack)[::-1]:
            fleet.append((target - p) / s)
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)      