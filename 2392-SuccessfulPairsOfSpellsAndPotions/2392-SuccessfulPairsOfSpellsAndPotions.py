# Last updated: 7/26/2025, 2:32:02 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Brute Force Approach - Sort the potions array, then check till potion[i] * spell of [i] > success
        # TC - O(s*p) where s and p are lengths of spell and potion, SC -  O(spells)
        # This solution can run for smaller input, will need optimal approach to control the time

        # s = len(spells)
        # p = len(potions)
        # potions.sort()

        # # print(potions)
        # result = []
        # for spell in spells:
        #     # print(spell)
        #     check = 0
        #     for i in range(p):
        #         if potions[i] * spell >= success:
        #             check = p - i 
        #             break

        #     result.append(check)
        # return result

        # Approach - Use Binary search on the potions array to skip testing in the loop for the non success generating ones.
        # TC - O(n+m(logm))  SC - O(len(spells))
        p = len(potions)
        potions.sort()
        result = []

        for spell in spells:
            left = 0
            right = p - 1
            check = p # To keep the value where we find the first val in potions where potions * spell

            # Binary search in the potions array to find the value from where we have success.
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid - 1
                    check = mid
                else:
                    left = mid + 1
            result.append(p - check)
        
        return(result)