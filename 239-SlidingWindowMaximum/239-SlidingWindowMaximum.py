# Last updated: 7/28/2025, 11:02:32 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach - Use a deque to store the values in the window, check for the max value and then keep on updating the deque when you slide the window
        # TC - O(n)
        # SC - O(n)

        q = collections.deque()
        n = len(nums)
        result = []
        l = r = 0
        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1 
        return result