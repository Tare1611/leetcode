# Last updated: 7/26/2025, 2:32:13 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        # Brute Force Approach - Use a for loop and store the old values in an array.
        # TC - O() SC - O()

        [0,1,1,2,4]
        trib = [0,1,1]
        # print(trib)
        if n <= 2:
            return trib[n]
        for i in range(3, n+1):
                # print(i)
                addTrib = trib[i - 1] + trib[i - 2] + trib[i - 3]
                trib.append(addTrib)
        # print(trib[n])
        return trib[n]
        