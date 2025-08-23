# Last updated: 8/23/2025, 1:21:35 PM
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Approach - Use counter to store the frequency of each element
        # - From the count and total remove the num to consider it as an outlier
        # - Check if the total of the nums array is divisible by 2
        # - Check if the integer division of total exist in the count hashMap
        # - Store the outlier value and repeat to find the largest value of the outlier.
        # TC - O(n)
        # SC - O(n)

        count = Counter(nums)
        total = sum(nums)
        outlier = float('-inf')

        for num in nums:
            # Removing num from calculation to consider it as the outlier
            count[num] -= 1
            total -= num

            if (total % 2 == 0) and count[total // 2] > 0:
                outlier = max(outlier, num)
            # Adding the num back to check for another num
            count[num] += 1
            total += num
            # print(outlier)
        return outlier 