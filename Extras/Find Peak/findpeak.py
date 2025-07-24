# Check for the peak in an integer array.
# Ideal case is that the array starts as a sorted array, reaches a peak and then starts to decrease. 
# Return the peak. If the array is empty then return "-1".
# The array edge case - array can be just sorted in asc and dsc. Also the array can contain duplicate values.

# Approach - Use binary search to control the TC - O(logn), the worst the TC could be O(n)

def findPeak(nums):
    if not nums:
        return -1
    
    n = len(nums)
    l = 0
    r = n-1
    mid = 0

    if all( nums[i] <= nums[i+1] for i in range(n-1)):
        return nums[-1]

    if all( nums[i] >= nums[i+1] for i in range(n-1)):
        return nums[0]
    
    while l < r:
        mid = l + r//2

        if nums[l] < nums[mid]:
            l = mid+1
        elif nums[mid] > nums[r]:
            r = mid-1
        else:
            r -= 1
    return nums[l]

nums = [1,2,3,4,5,4,3,2,1]
print(findPeak(nums))